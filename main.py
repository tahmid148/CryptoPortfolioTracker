import databaseHelper
from classes.order import Order

def main():
    print("main")
    df = databaseHelper.calculate_realised_profit_loss("ETH/USDT")
    print(df)
    databaseHelper.close_connection()



if __name__ == "__main__":
    main()
