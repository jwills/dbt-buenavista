
from typing import Any, Dict

from buenavista.adapter import Adapter
from buenavista.core import BuenaVistaServer

from .python_extension import DbtPythonRunner

def _duckdb_adapter(config: Dict[str, Any]) -> Adapter:
    from buenavista.backend.duckdb import DuckDBAdapter
    import duckdb

    db = duckdb.connect(config["path"])
    for e in config.get("extensions", []):
        db.install_extension(e)
        db.load_extension(e)
    for key, value in config.get("settings", {}).items():
        db.execute(f"SET {key} = '{value}'")
    return DuckDBAdapter(db)


def _postgres_adapter(config: Dict[str, Any]) -> Adapter:
    from buenavista.backend.postgres import PGAdapter
    kwargs = {}
    for k in ("host", "port", "user", "password", "dbname"):
        if k in config:
            kwargs[k] = config[k]
    return PGAdapter(**kwargs)


def create(bv_config: Dict[str, Any], backing_config: Dict[str, Any]) -> BuenaVistaServer:
    backing_type = backing_config["type"]
    if backing_type == "postgres":
        adapter = _postgres_adapter(backing_config)
    elif backing_type == "duckdb":
        adapter = _duckdb_adapter(backing_config)
    else:
        raise Exception(f"Unsupported backing type for Buena Vista: {backing_type}")
    
    server_address = (bv_config.get("host"), bv_config.get("port"))
    return BuenaVistaServer(server_address, adapter, extensions=[DbtPythonRunner()])


if __name__ == "__main__":
    import os

    from dbt.config.profile import Profile, read_profile
    from dbt.config.project import Project
    from dbt.config.renderer import ProfileRenderer
    from dbt.config.utils import parse_cli_vars
    from dbt.main import _build_base_subparser
    from dbt import flags

    # includes vars, profile, target
    parser = _build_base_subparser()
    args, _unknown = parser.parse_known_args()

    # dbt-core does os.chdir(project_dir) before reaching this location
    # from https://github.com/dbt-labs/dbt-core/blob/73116fb816498c4c45a01a2498199465202ec01b/core/dbt/task/base.py#L186
    project_root = os.getcwd()

    # from https://github.com/dbt-labs/dbt-core/blob/19c48e285ec381b7f7fa2dbaaa8d8361374136ba/core/dbt/config/runtime.py#L193-L203
    version_check = bool(flags.VERSION_CHECK)
    partial = Project.partial_load(project_root, verify_version=version_check)

    cli_vars: Dict[str, Any] = parse_cli_vars(getattr(args, "vars", "{}"))
    profile_renderer = ProfileRenderer(cli_vars)
    project_profile_name = partial.render_profile_name(profile_renderer)

    # from https://github.com/dbt-labs/dbt-core/blob/19c48e285ec381b7f7fa2dbaaa8d8361374136ba/core/dbt/config/profile.py#L423-L425
    profile_name = Profile.pick_profile_name(
        getattr(args, "profile", None), project_profile_name
    )
    raw_profiles = read_profile(flags.PROFILES_DIR)
    raw_profile = raw_profiles[profile_name]

    # from https://github.com/dbt-labs/dbt-core/blob/19c48e285ec381b7f7fa2dbaaa8d8361374136ba/core/dbt/config/profile.py#L287-L293
    target_override = getattr(args, "target", None)
    if target_override is not None:
        target_name = target_override
    elif "target" in raw_profile:
        target_name = profile_renderer.render_value(raw_profile["target"])
    else:
        target_name = "default"

    bv_dict = Profile._get_profile_data(raw_profile, profile_name, target_name)
    delegate = bv_dict.get("delegate")
    assert delegate, "bv_* targets must have a delegate field set"

    base_profile = Profile.from_raw_profiles(
        raw_profiles,
        profile_name,
        renderer=profile_renderer,
        target_override=delegate,
    )