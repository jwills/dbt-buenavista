from dbt.adapters.duckdb.impl import DuckDBAdapter  # type:ignore

from dbt.adapters.bv_duckdb.connections import BVDuckDBConnectionManager


class BVDuckDBAdapter(DuckDBAdapter):
    ConnectionManager = BVDuckDBConnectionManager