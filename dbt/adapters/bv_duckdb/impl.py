from dbt.adapters.duckdb.impl import DuckDBAdapter  # type:ignore

from dbt.adapters.buenavista import python_job
from dbt.adapters.bv_duckdb.connections import BVDuckDBConnectionManager
from dbt.contracts.connection import AdapterResponse


class BVDuckDBAdapter(DuckDBAdapter):
    ConnectionManager = BVDuckDBConnectionManager

    def submit_python_job(
        self, parsed_model: dict, compiled_code: str
    ) -> AdapterResponse:
        return python_job.submit(self, parsed_model, compiled_code)
