import sqlite3
import pandas as pd

# NOTE: Do not modify script. 
# Script is required to setup database required for the SQL Tutorials.ipynb notebook

# setup SQLITE Database
conn = sqlite3.connect("sales_analysis.db")
conn.row_factory = sqlite3.Row  #this for getting the column names!

# Read sample dataset into a database
df_customers = pd.read_csv("Sales Analysis Data/customers.csv", encoding="ISO-8859-1")
df_categories = pd.read_csv("Sales Analysis Data/categories.csv", encoding="ISO-8859-1")
df_employees = pd.read_csv("Sales Analysis Data/employees.csv", encoding="ISO-8859-1")
df_orderdetails = pd.read_csv("Sales Analysis Data/orderdetails.csv", encoding="ISO-8859-1")
df_orders = pd.read_csv("Sales Analysis Data/orders.csv", encoding="ISO-8859-1")
df_products = pd.read_csv("Sales Analysis Data/products.csv", encoding="ISO-8859-1")
df_shippers = pd.read_csv("Sales Analysis Data/shippers.csv", encoding="ISO-8859-1")
df_suppliers = pd.read_csv("Sales Analysis Data/suppliers.csv", encoding="ISO-8859-1")

# Upload dataframe in database
df_customers.to_sql("customers", conn, if_exists='replace', index=False,)
df_categories.to_sql("categories", conn, if_exists='replace', index=False,)
df_employees.to_sql("employees", conn, if_exists='replace', index=False,)
df_employees.to_sql("orderdetails", conn, if_exists='replace', index=False,)
df_orders.to_sql("orders", conn, if_exists='replace', index=False,)
df_products.to_sql("products", conn, if_exists='replace', index=False,)
df_shippers.to_sql("shippers", conn, if_exists='replace', index=False,)
df_suppliers.to_sql("suppliers", conn, if_exists='replace', index=False,)

# sql script execution functions 
def run_sql_script(sql):
    cur = conn.cursor()
    cur.execute(sql)    
 
    rows = cur.fetchall()
    columns = rows[0].keys()
    data = pd.DataFrame(rows,columns=columns)
    cur.close()
    return data