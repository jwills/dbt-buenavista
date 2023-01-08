
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