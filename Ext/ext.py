import oracledb
import json
import pandas as pd

with open("parameters.json", "r", encoding="utf-8") as f:
    config = json.load(f)

db = config["oracle"]

def conect(db):
    return oracledb.connect(
        user=db["user"],
        password=db["password"],
        host=db["host"],
        port=db["port"],
        service_name=db["service_name"]
    )

def ext_transactions():
    query = """
    SELECT transaction_id, customer_id, amount
    FROM transactions 
    WHERE status = 'ACTIVE'
    """
    df = pd.read_sql(query, conect(db))
    df = df.astype({
        "TRANSACTION_ID": "int64",
        "CUSTOMER_ID": "int64",
        "AMOUNT": "float64"
    })

    return df

def ext_customers():
    query = """
    SELECT customer_id, customer_name
    FROM customers 
    WHERE status = 'ACTIVE'
    """
    df = pd.read_sql(query, conect(db))
    df = df.astype({
        "CUSTOMER_ID": "int64",
        "CUSTOMER_NAME": "string"
    })
    return df