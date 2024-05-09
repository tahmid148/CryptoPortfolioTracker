import helpers.databaseHelper as databaseHelper
import helpers.exchangeHelper as exchangeHelper
from classes.order import Order


def main():
    print("main")
    exchangeHelper.get_pair_price('ETH/USDT', 'KUC')
    databaseHelper.close_connection()



if __name__ == "__main__":
    main()
