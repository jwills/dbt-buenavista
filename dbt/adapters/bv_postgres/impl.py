from dbt.adapters.postgres.impl import PostgresAdapter  # type:ignore

from common.python_job import PythonJobRunner
from dbt.adapters.bv_postgres.connections import BVPostgresConnectionManager
from dbt.contracts.connection import AdapterResponse


class BVPostgresAdapter(PostgresAdapter):
    ConnectionManager = BVPostgresConnectionManager

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