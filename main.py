import helpers.DatabaseHelper as DatabaseHelper
import helpers.ExchangeHelper as ExchangeHelper
import constants
from classes.order import Order


def main():
    exchangeHelper = ExchangeHelper.ExchangeHelper()

    eth_price = exchangeHelper.get_pair_price('ETH/USDT', constants.KUCOIN)
    print(eth_price)

if __name__ == "__main__":
    main()
