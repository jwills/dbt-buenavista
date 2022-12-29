from dbt.adapters.duckdb.impl import DuckDBAdapter  # type:ignore

from common.python_job import PythonJobRunner
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
        credentials = self.config.credentials
        base_url = f"http://{credentials.host}:{credentials.api_port}"
        runner = PythonJobRunner(base_url, connection.handle.get_backend_pid())
        return runner.submit(parsed_model, compiled_code)
