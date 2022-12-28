from dataclasses import dataclass

from dbt.adapters.postgres.connections import (  # type:ignore
    PostgresConnectionManager,
    PostgresCredentials,
)

@dataclass
class BVDuckDBCredentials(PostgresCredentials):
    @property
    def type(self) -> str:
        return "bv_duckdb"


class BVDuckDBConnectionManager(PostgresConnectionManager):
    TYPE = "bv_duckdb"