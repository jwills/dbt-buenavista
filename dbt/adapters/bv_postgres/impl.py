from dbt.adapters.postgres.impl import PostgresAdapter  # type:ignore

from dbt.adapters.bv_postgres.connections import BVPostgresConnectionManager


class BVPostgresAdapter(PostgresAdapter):
    ConnectionManager = BVPostgresConnectionManager