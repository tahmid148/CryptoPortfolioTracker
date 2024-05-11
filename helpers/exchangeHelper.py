import ccxt
import constants

class ExchangeHelper:
    def __init__(self):
        self.ccxt_kucoin = ccxt.kucoin()
        self.ccxt_mexc = ccxt.mexc()

    def get_pair_price(self, pair: str, exchange: str) -> int:
        if (exchange == constants.KUCOIN):
            last_price = self.ccxt_kucoin.fetch_ticker(pair)['last']
        elif exchange == constants.MEXC:
            last_price = self.ccxt_mexc.fetch_ticker(pair)['last']
        return last_price