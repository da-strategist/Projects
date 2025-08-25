import dagster as dg
import pandas as pd
import duckdb
from dagster_duckdb import DuckDBResource




@dg.asset(
    deps=["data_ingestion"],
)
def transformed_data(database: DuckDBResource) -> None:
    query = """
        CREATE OR REPLACE TABLE processed_retail_data AS
        SELECT * FROM './data/raw/retail_raw.csv'
    """
    with database.get_connection() as conn:
        conn.execute(query)
