
import pandas as pd
import dagster as dg
from dagster_duckdb import DuckDBResource
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential

#here we shall be uploading our dataset into azure blob storage