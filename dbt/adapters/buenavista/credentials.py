from dataclasses import dataclass
from typing import Optional

from dbt.adapters.base import Credentials
from dbt.helper_types import Port


@dataclass
class BVCredentials(Credentials):
    host: str
    port: Port

    # everything else on bv is optional atm
    user: Optional[str] = "dbt"
    password: Optional[str] = "password"

    # Used when we are running everything locally off of the profile.yml file
    api_port: Optional[int] = None
    delegate: Optional[str] = None  # on BV targets the delegate is mandatory

    # things copied over from the Postgres credentials
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
