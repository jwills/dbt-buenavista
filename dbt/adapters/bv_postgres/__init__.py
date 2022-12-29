# these are mostly just exports, #noqa them so flake8 will be happy
from dbt.adapters.bv_postgres.connections import BVPostgresConnectionManager  # noqa
from dbt.adapters.bv_postgres.connections import BVPostgresCredentials
from dbt.adapters.bv_postgres.impl import BVPostgresAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import bv_postgres

Plugin = AdapterPlugin(
    adapter=BVPostgresAdapter,
    credentials=BVPostgresCredentials,
    include_path=bv_postgres.PACKAGE_PATH,
    dependencies=["postgres"],
)
