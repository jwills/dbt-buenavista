from dataclasses import dataclass
from typing import Optional

from dbt.adapters.base import Credentials
from dbt.helper_types import Port

@dataclass
class BVCredentials(Credentials):
    host: str
    user: str
    port: Port
    password: str  # on postgres the password is mandatory
    delegate: str  # on BV targets the delegate is mandatory
    connect_timeout: int = 10
    role: Optional[str] = None
    search_path: Optional[str] = None
    keepalives_idle: int = 0  # 0 means to use the default value
    sslmode: Optional[str] = None
    sslcert: Optional[str] = None
    sslkey: Optional[str] = None
    sslrootcert: Optional[str] = None
    application_name: Optional[str] = "dbt"
    retries: int = 1

    _ALIASES = {"dbname": "database", "pass": "password"}

    @property
    def unique_field(self):
        return self.host

    def _connection_keys(self):
        return (
            "host",
            "port",
            "user",
            "database",
            "schema",
            "search_path",
            "keepalives_idle",
            "sslmode",
        )