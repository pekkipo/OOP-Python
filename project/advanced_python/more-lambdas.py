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


def _get_currency_resource(resource, transform=(lambda x:x)):
    # transform is a func. By default it will just leave values unchanged

    # requests.get(....).json() # Imagine getting some info

    # say we get the response like:
    data = {
            'items': [
                {'code':'usd', 'amount_to_usd':1.00},
                {'code':'gbp', 'amount_to_usd': 1.21},
            ]
    }

    my_resource = data[resource]
    # return list(map(transform, my_resource)) # same as stuff below
    # map applies the func transform to all the elements of the list
    return [transform(x) for x in my_resource]


def get_currency_codes():
    return _get_currency_resource('items', lambda x: x['code'].upper())

#currencies = _get_currency_resource('items') # will use default transform func so nothing changes

#currencies = _get_currency_resource('items', lambda x: x['code'].upper())
# will change the currency code - makes it uppercase

print(get_currency_codes())

# getting currency objects
def get_currencies():
    return _get_currency_resource('items', lambda x: Currency(x['code'], x['amount_to_usd']))
    # turn every dict into a Currency object and return the list

def calculate_in_all_currencies(usd_amount):
    print("-- {} USD in all currencies --".format(usd_amount))
    for currency in get_currencies():
        print("In {}: {:.2f}".format(currency.code, currency.in_currency(usd_amount)))


calculate_in_all_currencies(5000)