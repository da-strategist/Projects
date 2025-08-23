
import ssl_patch
import dagster as dg
from assets import data_extraction
from resources import database_resource


all_assets = dg.load_assets_from_modules([data_extraction])




defs = dg.Definitions(
    assets=all_assets,
    resources={
        "database": database_resource
    }
)
