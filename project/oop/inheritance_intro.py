class Decimal:
    def __init__(self, number, places):
        self.number = number
        self.places = places

    def __repr__(self):
        return "%.{}f".format(self.places) % self.number


class Curr(Decimal):
    # inherited from Decimal. Has all its props and methods

    def __init__(self, symbol, number, places):
        super().__init__(number, places)
        # necessary to inlcude parent class props
        # can play around with those values in super.init
        # can do number - 1 for instance
        self.symbol = symbol
        # property of Currency specifically

    def __repr__(self): # override repr method of Decimal
        return "{}{}".format(self.symbol, super().__repr__())
        # called a method of a parent Decimal class


    def add_currency(self, currency):
        # availabe for Currency class
        # not available for Decimal class
        pass




print(Decimal(15.6789,3))