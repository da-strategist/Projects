import dagster as dg
import pandas as pd
import duckdb
from dagster_duckdb import DuckDBResource



@dg.asset(
        deps=["data_ingestion"],
        required_resource_keys={"database"},
          )
def transform_data(context, data_ingestion) -> None:

    conn = context.resources.database
    conn.register("retail_data_processed", data_ingestion)
    conn.execute(
        """
        create or replace table retail_data_processed as
        SELECT * FROM my_data
        """
    )
    conn.close()