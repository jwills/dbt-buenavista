from dbt.adapters.postgres.impl import PostgresAdapter  # type:ignore

from common import python_job
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
        return python_job.submit(connection, self.config.credentials, parsed_model, compiled_code)