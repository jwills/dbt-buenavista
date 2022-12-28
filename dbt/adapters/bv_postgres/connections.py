from dataclasses import dataclass

from dbt.adapters.postgres.connections import (  # type:ignore
    PostgresConnectionManager,
    PostgresCredentials,
)

@dataclass
class BVPostgresCredentials(PostgresCredentials):
    @property
    def type(self) -> str:
        return "bv_postgres"


class BVPostgresConnectionManager(PostgresConnectionManager):
    TYPE = "bv_postgres"