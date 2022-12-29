from dataclasses import dataclass

from dbt.adapters.postgres.connections import (  # type:ignore
    PostgresConnectionManager,
    PostgresCredentials,
)
from dbt.helper_types import Port

@dataclass
class BVDuckDBCredentials(PostgresCredentials):
    api_port: Port = 8000

    @property
    def type(self) -> str:
        return "bv_duckdb"


class BVDuckDBConnectionManager(PostgresConnectionManager):
    TYPE = "bv_duckdb"
