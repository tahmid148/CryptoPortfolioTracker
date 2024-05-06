import mysql.connector
import pandas as pd
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
def get_all_rows() -> pd.DataFrame:
    query = "SELECT * FROM Orders"
    return pd.read_sql_query(query, connnection)
    

# Calculate unrealised profit/loss for a given pair
def calculate_unr_profit_loss(pair, currentPrice):
    df = get_all_rows()
    filtered_df = df[df['PAIR'] == pair]
    buy_df = filtered_df[filtered_df['SIDE'] == 'BUY']
    sell_df = filtered_df[filtered_df['SIDE'] == 'SELL']
    
    total_buy_size = buy_df['SIZE'].sum()
    total_sell_size = sell_df['SIZE'].sum()
    current_size = total_buy_size - total_sell_size
    
    # Remaining size
    print(current_size)

    # Find the average buy price
    average_buy_price = (buy_df['SIZE'] / total_buy_size) * (buy_df ['PRICE'])

    return (current_size * currentPrice) - average_buy_price.sum()

def calculate_realised_profit_loss(pair):
    df = get_all_rows()
    filtered_df = df[df['PAIR'] == pair]
    buy_df = filtered_df[filtered_df['SIDE'] == 'BUY']
    sell_df = filtered_df[filtered_df['SIDE'] == 'SELL']

    total_buy_size = buy_df['SIZE'].sum()
    total_sell_size = sell_df['SIZE'].sum()
    
    # Calculate the weighted average buy price
    average_buy_price = (buy_df['SIZE'] * buy_df['PRICE']).sum() / total_buy_size
    
    # Calculate the total cost basis for the sold ETH
    total_cost_of_sold = average_buy_price * total_sell_size
    
    # Calculate the total revenue from sold ETH
    total_revenue_from_sales = (sell_df['SIZE'] * sell_df['PRICE']).sum()
    
    # Calculate realized profit or loss
    realized_profit_loss = total_revenue_from_sales - total_cost_of_sold

    return realized_profit_loss


    
def close_connection():
    connnection.close()
