import pandas as pd
import numpy as np
from extract import extract

datasets = extract()

resultado_1 = datasets["sales"].merge(datasets["customers"], on="customer_id")
resultado_2 = resultado_1.merge(datasets["sales_items"], on="sale_id")

# drop y columns and rename x columns to avoid confusion
resultado_2 =  resultado_2.drop(columns=["sale_date_y", "discounted_y", "channel_y"])
resultado_2 = resultado_2.rename(columns={"channel_x": "channel", "sale_date_x": "sale_date", "discounted_x": "discounted", "country_x": "country_sales", "country_y": "country_customers"})


resultado_3 = resultado_2.merge(datasets["products"], on="product_id")
resultado_4 = resultado_3.merge(datasets["channels"], on="channel")

#creating cost_total and profit columns 
resultado_4["cost_total"]= resultado_4["cost_price"] * resultado_4["quantity"]
resultado_4["profit"] = resultado_4["item_total"] - resultado_4["cost_total"]

##resultado_4["discount"] = (
 ## resultado_4["discount"].str.replace("%", "", regex=False)
 ## .astype(float)
 ##)

resultado_4["sale_date"] = pd.to_datetime(resultado_4["sale_date"])
resultado_4["year"] = resultado_4["sale_date"].dt.year
resultado_4["month"] = resultado_4["sale_date"].dt.month
resultado_4["quarter"] = resultado_4["sale_date"].dt.quarter
resultado_4["week"] = resultado_4["sale_date"].dt.isocalendar().week
resultado_4["day"] = resultado_4["sale_date"].dt.day

print(resultado_4)