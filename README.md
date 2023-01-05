## dbt-buenavista

[Buena Vista](http://github.com/jwills/buenavista) is a Postgres proxy server written in Python. It is designed to
live between a data warehouse and downstream data consumers (BI tools, cron jobs, notebooks, etc.) in order to give
data teams the power and flexibility

[dbt](http://getdbt.com) is the best way to manage a collection of data transformations written in SQL or Python for analytics
and data science. Combining Buena Vista with dbt allows analytics engineers and data scientists t

### Installation

The latest supported version targets `dbt-core` 1.3.x and `duckdb` version 0.5.x, but we work hard to ensure that newer

### Configuring Your Profile

The profile settings for a dbt-buenavista connection are identical to the settings for a
[dbt-postgres profile](https://docs.getdbt.com/reference/warehouse-setups/postgres-setup#profile-configuration), since every
`dbt-buenavista` adapter is a subclass of the `dbt-postgres` adapter. Instead of setting the profile's `type` field as
`postgres`, you set it to one of the Buena Vista supported types, which are currently `bv_duckdb` (for a Buena Vista server
powered by DuckDB) or `bv_postgres` (for a Buena Vista server that is proxying a Postgres database.) The `host`, `port`, `user`,
and `password` settings are all required and should be configured to point at the Buena Vista server that you are using.

````
default:
  outputs:
   dev:
     type: <bv_duckdb|bv_postgres>
     host: <host>
     port: <port>
     user: <user>
     password: <password>
     dbname: <dbname>
     ...
  target: dev
````
