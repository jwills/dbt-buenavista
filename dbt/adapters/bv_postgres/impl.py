from dbt.adapters.postgres.impl import PostgresAdapter  # type:ignore

from common.python_job import PythonJobMixin
from dbt.adapters.bv_postgres.connections import BVPostgresConnectionManager


class BVPostgresAdapter(PostgresAdapter, PythonJobMixin):
    ConnectionManager = BVPostgresConnectionManager
