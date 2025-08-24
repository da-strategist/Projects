import dagster as dg
from dagster_duckdb import DuckDBResource


database_resource = DuckDBResource(database="./data/staging/transformed_data.duckdb")


@dg.definitions
def resources():
     return dg.Definitions(resources={"database": database_resource})



