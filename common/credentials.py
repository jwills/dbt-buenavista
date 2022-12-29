from dataclasses import dataclass

from dbt.adapters.base import Credentials
from dbt.helper_types import Port


@dataclass
class BVCredentials(Credentials):
    host: str
    user: str
    port: Port
    api_port: Port

    def _connection_keys(self):
        return (
            "host",
            "port",
            "user",
            "database",
            "schema",
            "api_port",
        )
