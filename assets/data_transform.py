import dagster as dg
import pandas as pd
import duckdb
from dagster_duckdb import DuckDBResource




@dg.asset(
    deps=["data_ingestion"],
    required_resource_keys={"database"},
)
def transform_data(context, data_ingestion) -> None:
    with context.resources.database.get_connection() as conn:
        conn.register("my_data", data_ingestion)
        conn.execute("""
            create or replace table retail_data_processed as
            select * from my_data
        """)




@dg.asset(
    deps=["data_ingestion"],
)
def transformed_data(database: DuckDBResource) -> None:
    query = """
        CREATE OR REPLACE TABLE processed_retail_data AS
        SELECT * FROM retail_raw
    """
    with database.get_connection() as conn:
        conn.execute(query)