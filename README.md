## dbt-buenavista

[Buena Vista](http://github.com/jwills/buenavista) is a Postgres proxy server written in Python. It is intended to
serve as the Controller in the [Model-View-Controller architecture](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
for data applications, providing a locus of control for data teams in between the data warehouse (model layer) and downstream
data consumers like BI tools and notebooks (view layer.)

[dbt](http://getdbt.com) is the best way to manage a collection of data transformations written in SQL or Python for analytics
and data science.

The purpose of `dbt-buenavista` is to explore some new techniques for creating dbt models that a proxy service like
Buena Vista makes possible, starting with a new way of executing dbt's Python models inspired by the approach taken
by [dbt-duckdb](http://github.com/jwills/dbt-duckdb): instead of pushing the Python compute into the Python execution engines
supported by Snowflake, Databricks, and BigQuery, the dbt-buenavista adapter executes the Python models on the Buena Vista
server itself, reading in any data tables that are used in the computation as data frames (either Pandas or another data frame
library supported by the data warehouse) and writing the data frame back to the data warehouse when the computation is finished.
This approach makes it possible to support Python-based models against data warehouses that do not ship with a Python execution
engine (most notably Postgres and Redshift) and may well simplify the development and debugging workflows for teams that want to
include Python models in their data pipelines (e.g., `print` and `logging` statements will run on the Buena Vista server and can
be sent wherever they need to go to aid in debugging.)

### Installation

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
