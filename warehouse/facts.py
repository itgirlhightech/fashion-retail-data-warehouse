import pandas as pd
import sys
import os

# find files inside the src path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from extract import extract
from transform import transform

datasets = extract()
resultado_4 = transform(datasets)

fact_sales = resultado_4[[
    "sale_id", "item_id", "customer_id", "product_id", "channel",
    "sale_date", "quantity", "unit_price", "original_price", 
    "item_total", "cost_total", "profit", "discount_percent"
]]

print(fact_sales.shape)