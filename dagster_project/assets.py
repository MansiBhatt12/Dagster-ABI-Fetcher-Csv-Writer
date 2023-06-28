#Dagster project to fetch HTTP requests and interacting with APIs (fetch all ABIs available open source for 5 contract_addresses)
#and save your data to a csv file, Store it in database (for our case they can just return a dataframe) 
#with Dataframes and interacting with them (pandas -> polars)
#also schedule your pipeline, define a job  and schedule to run assigned job at every hour
#and Manage your own I/O so you can save your data in more permanent location


import requests
import csv
import pandas as pd
import polars as pl

from dagster import asset

api_key = "M2Z69469HXICTNG2WJC9BC6IWECE3QY2K7"
contract_addresses = [
    "0x889f3c7ab880153cbd7db7270bfbf22760fda169",
    "0x99a679f5977841f55db7ce2d56fa85c96ca7f104",
    "0xc669eaad75042be84daaf9b461b0e868b9ac1871",
    "0x45109a940501da9c2f32db25fb40c23c5775a62c",
    "0xd8563be89a5cd66874d78b58af57a9add3286e03",
]

def fetch_api(contract_address) :
    url = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    

@asset
def contract_api_assets():
    apis = []
    for contract_address in contract_addresses:
        api = fetch_api(contract_address)
        if api is not None:
            apis.append(api)
    

    with open("data/api.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for row in apis:
            writer.writerow(row.values())

    df = pd.DataFrame(apis)
    pl_df = pl.from_pandas(df)

    print(pl_df)

    return pl_df
