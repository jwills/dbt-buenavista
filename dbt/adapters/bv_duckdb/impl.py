from dbt.adapters.duckdb.impl import DuckDBAdapter  # type:ignore

from common import python_job
from dbt.adapters.bv_duckdb.connections import BVDuckDBConnectionManager
from dbt.contracts.connection import AdapterResponse


class BVDuckDBAdapter(DuckDBAdapter):
    ConnectionManager = BVDuckDBConnectionManager

    def submit_python_job(
        self, parsed_model: dict, compiled_code: str
    ) -> AdapterResponse:
        connection = self.connections.get_if_exists()
        if not connection:
            connection = self.connections.get_thread_connection()
        return python_job.submit(connection, self.config.credentials, parsed_model, compiled_code)