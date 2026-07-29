# Fashion Retail Data Warehouse with Apache Airflow

End-to-end Data Engineering project that builds a Data Warehouse for a fashion retail company using a dimensional model (Star Schema), ETL pipelines in Python, SQL reporting, and workflow orchestration with Apache Airflow.

---

## Project Overview

This project demonstrates the complete lifecycle of a modern data engineering solution:

- Extract data from multiple CSV files.
- Transform and clean datasets using Python and Pandas.
- Build dimension and fact tables.
- Load the processed data into a PostgreSQL Data Warehouse.
- Orchestrate the ETL pipeline using Apache Airflow.
- Generate analytical SQL reports for business insights.

The objective is to simulate a real-world retail analytics environment while applying data engineering best practices.

---

## Tech Stack

- Python 3.12
- Pandas
- PostgreSQL
- Apache Airflow
- SQL
- SQLAlchemy
- Python-dotenv
- Git & GitHub

---

## Project Structure

```text
fashion-retail-data-warehouse/
│
├── airflow_home/
│   └── dags/
│
├── data/
│   └── raw/
│
├── docs/
│
├── sql/
│   └── reports.sql
│
├── src/
│   ├── database.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── warehouse/
│   ├── dimensions.py
│   └── facts.py
│
├── README.md
└── requirements.txt
```

---


## How to Run

```bash
# 1. Clone the repository and set up the virtual environment
git clone https://github.com/itgirlhightech/fashion-retail-data-warehouse.git
cd fashion-retail-data-warehouse
python -m venv airflow_venv
source airflow_venv/bin/activate
pip install -r requirements.txt

# 2. Set up environment variables
# Create a .env file in the project root with:
# DB_USER=your_user
# DB_PASSWORD=your_password
# DB_HOST=localhost
# DB_PORT=5432
# DB_NAME=your_database_name

# 3. Create the PostgreSQL database
sudo -u postgres psql
# CREATE DATABASE your_database_name;
# CREATE USER your_user WITH PASSWORD 'your_password';
# GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_user;
# GRANT ALL PRIVILEGES ON SCHEMA public TO your_user;
# \q

# 4. Start Airflow
export AIRFLOW_HOME=$(pwd)/airflow_home
airflow standalone

# 5. Trigger the pipeline
# Via the web UI at localhost:8080, or via terminal:
airflow dags trigger fashion_retail_pipeline
```

Once the DAG completes successfully, the 5 tables (`dim_customer`, `dim_product`, `dim_channel`, `dim_date`, `fact_sales`) will be available in PostgreSQL, ready for querying via `sql/reports.sql`.

---

# Architecture

```mermaid
flowchart LR

A[Raw CSV Files]
--> B[Extract]

B --> C[Transform]

C --> D[Dimension Tables]

C --> E[Fact Table]

D --> F[(PostgreSQL)]

E --> F

F --> G[Apache Airflow]

```
```mermaid
erDiagram
    FACT_SALES {
        int sale_id
        int item_id
        int customer_id FK
        int product_id FK
        string channel FK
        date sale_date
        int quantity
        float item_total
        float cost_total
        float profit
    }

    DIM_CUSTOMER {
        int customer_id PK
        string age_range
        date signup_date
        string country_customers
    }

    DIM_PRODUCT {
        int product_id PK
        string product_name
        string category
        string brand
        float catalog_price
        float cost_price
    }

    DIM_CHANNEL {
        string channel PK
        string description
    }

    DIM_DATE {
        date date PK
        int year
        int month
        int quarter
        int week
    }

    DIM_CUSTOMER ||--o{ FACT_SALES : "faz"
    DIM_PRODUCT ||--o{ FACT_SALES : "vendido em"
    DIM_CHANNEL ||--o{ FACT_SALES : "ocorre via"
    DIM_DATE ||--o{ FACT_SALES : "acontece em"
```

---

# Star Schema

![Star Schema](docs/star_schema.svg)


---

# Apache Airflow DAG

The ETL pipeline is orchestrated using Apache Airflow.

Pipeline tasks:

1. Extract Data
2. Transform Data
3. Dimensions and fact
4. Load Data

---

# Airflow Execution




![Airflow Graph](docs/airflow_graph.png)

![Airflow DAG](docs/airflow1.png)


---


# Data Warehouse Model

The dimensional model consists of:

### Dimensions

- dim_customer
- dim_product
- dim_channel
- dim_date

### Fact

- fact_sales

This structure enables fast analytical queries while reducing redundancy.


---

# Future Improvements

- Docker support
- Automated testing
- BI dashboard integration
- Incremental loading
- Logging improvements
- CI/CD with GitHub Actions
- Cloud deployment (AWS)

---

# Learning Outcomes

This project demonstrates practical experience with:

- ETL development
- Data Warehousing
- Star Schema modeling
- PostgreSQL
- Apache Airflow
- SQL Analytics
- Python for Data Engineering
- Workflow orchestration
- Git version control

---

## Dataset

This project uses the **European Fashion Store Multi-Table Dataset** available on Kaggle.

**Source:**
https://www.kaggle.com/datasets/joycemara/european-fashion-store-multitable-dataset

The dataset simulates transactions from an online fashion retailer and includes information about customers, products, orders, channels and inventory. It was adapted for building a dimensional model, ETL pipeline and analytical warehouse.