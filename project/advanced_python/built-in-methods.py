class Currency:
    def __init__(self, code, exchange_to_usd):
        self.amount = 0.00
        self.code = code
        self.exchange_to_usd = exchange_to_usd

    def set_amount(self, amount):
        self.amount = amount


    def in_currency(self, amount):
        # amount in USD to the currency in exchange_to_usd
        return amount / self.exchange_to_usd

    def to_usd(self, amount = None):
        to_convert = amount if amount is not None else self.amount
        # use parameter or if par is None then use the property
        # amount of dollars
        return amount * self.exchange_to_usd

    # we what to do pounds > euros
    # we tell how to compare objects
    # gt - greater than
    def __gt__(self, other): # other is a Python name
        return self.to_usd() > other.to_usd()

    # less than
    def __lt__(self, other):
        pass

    # less than or equal to
    def __le__(self, other):
        pass

    # greate than or equal to
    def __ge__(self, other):
        pass

    # equal ==
    def __eq__(self, other):
        return self.to_usd() == other.to_usd()
    # returns boolean


pounds = Currency("GBP", 1.21) # 1.21 exchange rate
euros = Currency("EUR", 1.07)

print(pounds > euros)
