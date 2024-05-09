import ccxt

def get_pair_price(pair, exchange):
    kucoin = ccxt.kucoin()
    print(kucoin.fetch_ticker(pair)['last'])