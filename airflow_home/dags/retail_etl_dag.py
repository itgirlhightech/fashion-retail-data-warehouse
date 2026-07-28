from airflow.decorators import dag, task
from datetime import datetime as dt 

import os
import sys
import pickle

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)
sys.path.insert(0, PROJECT_ROOT)

from src.extract import extract
from src.transform import transform
from warehouse.dimensions import build_dimensions
from warehouse.facts import build_facts
from src.load import load


TEMP_DIR = "/tmp/fashion_dw"
os.makedirs(TEMP_DIR, exist_ok=True)

# TaskFlow API 

@dag(
    dag_id="fashion_retail_pipeline",
    start_date=dt(2026, 1, 1),
    schedule=None,
    catchup=False,
)
def fashion_retail_pipeline():
    @task
    def run_extract():
        datasets = extract()
        caminho = os.path.join(TEMP_DIR, "datasets.pkl")
        with open(caminho, "wb") as f:
            pickle.dump(datasets, f)
        return caminho

    @task
    def run_transform(caminho_datasets: str):
        with open(caminho_datasets, "rb") as f:
            datasets = pickle.load(f)
        resultado_4 = transform(datasets)
        caminho = os.path.join(TEMP_DIR, "resultado_4.pkl")
        with open(caminho, "wb") as f:
            pickle.dump(resultado_4, f)
        return caminho

    @task
    def run_dimensions_facts(caminho_resultado: str):
        with open(caminho_resultado, "rb") as f:
            resultado_4 = pickle.load(f)

        dim_customer, dim_product, dim_channel, dim_date = build_dimensions(resultado_4)
        fact_sales = build_facts(resultado_4)
        
        caminhos = {}
        tabelas = {
            "dim_customer": dim_customer,
            "dim_product": dim_product,
            "dim_channel": dim_channel,
            "dim_date": dim_date,
            "fact_sales": fact_sales,
        }
        for nome, tabelas in tabelas.items():
            caminho = os.path.join(TEMP_DIR, f"{nome}.pkl")
            with open(caminho, "wb") as f:
                pickle.dump(tabela, f)
            caminhos[nome] = caminho

        return caminhos

    @task
    def run_load(caminhos_tabelas: dict):
        tabelas = {}
        for nome, caminho in caminhos_tabelas.items():
            with open(caminho, "rb") as f:
                tabelas[nome] = pickle.load(f)

        load(
            tabelas["dim_customer"],
            tabelas["dim_product"],
            tabelas["dim_channel"],
            tabelas["dim_date"],
            tabelas["fact_sales"],
        )

    caminho_datasets = run_extract()
    caminho_resultado = run_transform(caminho_datasets)
    caminhos_tabelas = run_dimensions_facts(caminho_resultado)
    run_load(caminhos_tabelas)

fashion_retail_pipeline()

