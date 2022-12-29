from dataclasses import dataclass

from dbt.adapters.postgres.connections import (  # type:ignore
    PostgresConnectionManager,
    PostgresCredentials,
)
from dbt.helper_types import Port

@dataclass
class BVPostgresCredentials(PostgresCredentials):
    api_port: Port = 8000

    @property
    def type(self) -> str:
        return "bv_postgres"


class BVPostgresConnectionManager(PostgresConnectionManager):
    TYPE = "bv_postgres"
