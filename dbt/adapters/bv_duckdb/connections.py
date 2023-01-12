from dataclasses import dataclass

from dbt.adapters.buenavista.credentials import BVCredentials
from dbt.adapters.postgres.connections import (  # type:ignore
    PostgresConnectionManager,
)


@dataclass
class BVDuckDBCredentials(BVCredentials):
    @property
    def type(self) -> str:
        return "bv_duckdb"


class BVDuckDBConnectionManager(PostgresConnectionManager):
    TYPE = "bv_duckdb"
