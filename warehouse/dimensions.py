import pandas as pd
import sys
import os

# find files inside the src path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from extract import extract
from transform import transform

datasets = extract()
resultado_4 = transform(datasets)

dim_customer = resultado_4[["customer_id", 
                            "age_range", 
                             "signup_date",
                              "country_customers"]
                              ].drop_duplicates()

dim_product = resultado_4[["product_id",
                            "product_name",
                             "category", "brand",
                             "color", "size",
                             "catalog_price", "cost_price", 
                             "gender"]].drop_duplicates()


dim_channel = resultado_4[["channel",
                           "description"]].drop_duplicates()


min_date = resultado_4["sale_date"].min()
max_date = resultado_4["sale_date"].max()
sequence = pd.date_range(start=min_date, end=max_date, freq="D")

dim_date = pd.DataFrame({"date": sequence })
dim_date["year"] = dim_date["date"].dt.year
dim_date["month"] = dim_date["date"].dt.month
dim_date["quarter"] = dim_date["date"].dt.quarter
dim_date["week"] = dim_date["date"].dt.isocalendar().week
dim_date["day"] = dim_date["date"].dt.day


