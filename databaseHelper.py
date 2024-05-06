import mysql.connector
import pandas as pd
from typing import List
from classes.order import Order


# Establish connection
connnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="Orders"
)

if connnection.is_connected():
    print("Connected to MySQL server")
else:
    print("Failed to connect to MySQL server")

# Insert a row into the Orders table
def insert_row(date, pair, side, price, size):
    cursor = connnection.cursor()
    
    insert_query = """
        INSERT INTO Orders (`DATE`, `PAIR`, `SIDE`, `PRICE`, `SIZE`)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (date, pair, side, price, size)
    cursor.execute(insert_query, values)
    connnection.commit()
    cursor.close()

# Returns a dataframe of all rows in Orders table
def get_all_rows() -> List[Order]:
    cursor = connnection.cursor()

    query = "SELECT * FROM Orders"
    cursor.execute(query)
    rows = cursor.fetchall()

    orders = []
    for row in rows:
        orders.append(Order(row[0], row[1], row[2], row[3], row[4]))

    cursor.close()
    return orders

def close_connection():
    connnection.close()
