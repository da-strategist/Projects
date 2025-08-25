import numpy as np
import pandas as pd
import dagster as dg
import requests



# the assets created here will be used to ingest our dataset from the retail sales API

@dg.asset
def data_ingestion() -> pd.DataFrame:
    url = "https://data.montgomerycountymd.gov/api/views/v76h-r7br/rows.csv?accessType=DOWNLOAD"
    retail_raw = pd.read_csv(url)

    retail_raw.to_csv("./data/raw/retail_raw.csv", index=False)

    return retail_raw

