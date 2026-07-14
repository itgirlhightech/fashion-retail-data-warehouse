import pandas as pd
from src.extract import extract

datasets = extract()

resultado_1 = datasets["sales"].merge(datasets["customers"], on="customer_id")
print(resultado_1.head())
print(resultado_1.head())