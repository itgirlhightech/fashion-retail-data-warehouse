import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "warehouse"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "database"))

from extract import extract
from transform import transform
from dimensions import dim_customer, dim_product, dim_channel, dim_date
from facts import fact_sales
from database import engine 

def load(
    dim_customer,
    dim_product,
    dim_channel,
    dim_date,
    fact_sales
):
    dim_customer.to_sql(
        name="dim_customer",
        con=engine,
        if_exists="replace",
        index=False
    )

    dim_product.to_sql(
        name="dim_product",
        con=engine,
        if_exists="replace",
        index=False
    )

    dim_channel.to_sql(
        name="dim_channel",
        con=engine,
        if_exists="replace",
        index=False
    )

    dim_date.to_sql(
        name="dim_date",
        con=engine,
        if_exists="replace",
        index=False
    )

    fact_sales.to_sql(
        name="fact_sales",
        con=engine,
        if_exists="replace",
        index=False
    )

if __name__ == "__main__":
    load(dim_customer, dim_product, dim_channel, dim_date, fact_sales)
    print("Tabelas carregadas com sucesso no PostgreSQL")


