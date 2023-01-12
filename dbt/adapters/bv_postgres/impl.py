from dbt.adapters.postgres.impl import PostgresAdapter  # type:ignore

from dbt.adapters.buenavista import python_job
from dbt.adapters.bv_postgres.connections import BVPostgresConnectionManager
from dbt.contracts.connection import AdapterResponse


class BVPostgresAdapter(PostgresAdapter):
    ConnectionManager = BVPostgresConnectionManager

    def submit_python_job(
        self, parsed_model: dict, compiled_code: str
    ) -> AdapterResponse:
        return python_job.submit(self, parsed_model, compiled_code)
