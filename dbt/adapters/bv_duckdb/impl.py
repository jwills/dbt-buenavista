from dbt.adapters.duckdb.impl import DuckDBAdapter  # type:ignore

from common.python_job import PythonJobMixin
from dbt.adapters.bv_duckdb.connections import BVDuckDBConnectionManager


class BVDuckDBAdapter(DuckDBAdapter, PythonJobMixin):
    ConnectionManager = BVDuckDBConnectionManager
