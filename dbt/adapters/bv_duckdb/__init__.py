# these are mostly just exports, #noqa them so flake8 will be happy
from dbt.adapters.bv_duckdb.connections import BVDuckDBConnectionManager  # noqa
from dbt.adapters.bv_duckdb.connections import BVDuckDBCredentials
from dbt.adapters.bv_duckdb.impl import BVDuckDBAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import bv_duckdb

Plugin = AdapterPlugin(
    adapter=BVDuckDBAdapter,
    credentials=BVDuckDBCredentials,
    include_path=bv_duckdb.PACKAGE_PATH,
    dependencies=["duckdb"],
)
