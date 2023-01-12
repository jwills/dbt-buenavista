from dataclasses import dataclass

from dbt.adapters.buenavista.credentials import BVCredentials
from dbt.adapters.postgres.connections import (  # type:ignore
    PostgresConnectionManager,
)


@dataclass
class BVPostgresCredentials(BVCredentials):
    @property
    def type(self) -> str:
        return "bv_postgres"


class BVPostgresConnectionManager(PostgresConnectionManager):
    TYPE = "bv_postgres"
