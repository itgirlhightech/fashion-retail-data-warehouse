import pandas as pd

# read csv files

campaigns = pd.read_csv("data/raw/dataset_fashion_store_campaigns.csv")
channels = pd.read_csv("data/raw/dataset_fashion_store_channels.csv")
customers = pd.read_csv("data/raw/dataset_fashion_store_customers.csv")
products = pd.read_csv("data/raw/dataset_fashion_store_products.csv")
sales = pd.read_csv("data/raw/dataset_fashion_store_sales.csv")
sales_items = pd.read_csv("data/raw/dataset_fashion_store_salesitems.csv")
stock = pd.read_csv("data/raw/dataset_fashion_store_stock.csv")