import databaseHelper
from classes.order import Order

def main():
    print("main")
    profit = databaseHelper.get_current_holdings()
    print(profit)
    databaseHelper.close_connection()



if __name__ == "__main__":
    main()
