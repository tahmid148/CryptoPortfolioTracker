class Order:
    def __init__(self, date, pair, side, price, size):
        self.date = date    # Date and time of the order
        self.pair = pair    # Trading pair (e.g., 'ETH/USDT')
        self.side = side    # Order side ('BUY', 'SELL', 'SEND', etc.)
        self.price = price  # Price of the order
        self.size = size    # Size of the order

    def __str__(self):
        return f"Date: {self.date}, Pair: {self.pair}, Side: {self.side}, Price: {self.price}, Size: {self.size}"
