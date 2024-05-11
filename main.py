import helpers.DatabaseHelper as DatabaseHelper
import helpers.ExchangeHelper as ExchangeHelper
import constants
from classes.order import Order


def main():
    exchangeHelper = ExchangeHelper.ExchangeHelper()
    databaseHelper = DatabaseHelper.DatabaseHelper()

    holdings_df = databaseHelper.get_current_holdings()
    holdings_df['Price'] = holdings_df['Pair'].apply(lambda x: exchangeHelper.get_pair_price(x, constants.KUCOIN)) * holdings_df['Size']
    holdings_df['Allocation'] = (holdings_df['Price'] / (holdings_df['Price'].sum())) * 100
    print(holdings_df)
    

if __name__ == "__main__":
    main()
