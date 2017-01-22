
import unittest



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


# Test word is important
class CurrencyTest(unittest.TestCase):
    # test word in necessary
    def test_create_currency(self):
        pounds = Currency('GBP', 1.21)

        # What needs to be verified.
        # We say something must equal something
        self.assertEqual(pounds.code, 'GBP')
        self.assertEqual(pounds.exchange_to_usd, 1.21)

    def test_set_amount(self):
        pounds = Currency('GBP', 1.21)
        euros = Currency('GBP', 1.07)

        pounds.set_amount(5000)
        euros.set_amount(10)

        self.assertEqual(pounds.amount, 5000)
        self.assertEqual(euros.amount, 10)

        # Assert True
        self.assertTrue(pounds > euros)
        self.assertFalse(pounds < euros)
        self.assertFalse(pounds == euros)

    def test_compare_currency_equal_value(self):
        pounds = Currency('GBP', 1.21)
        pounds2 = Currency('GBP', 1.21)

        pounds.set_amount(500)
        pounds2.set_amount(500)

        self.assertTrue(pounds >= pounds2)
        self.assertTrue(pounds <= pounds2)
        self.assertTrue(pounds == pounds2)

        self.assertFalse(pounds > pounds2)
        self.assertFalse(pounds < pounds2)

    def test_in_currency(self):
        pounds = Currency('GBP', 1.21)

        self.assertEqual(pounds.in_currency(1210), 1000)

    def test_to_usd(self):
        pounds = Currency('GBP', 1.21)

        self.assertEqual(pounds.to_usd(1000), 1210)


    # Testing methods that raise exceptions
    # We want to make sure that the exception will be caught if smth is wrong

    def comparison_with_exceptions(self):
        pounds = Currency('GBP', 1.21)
        pounds.set_amount(1000)

        with self.assertRaises(AttributeError):
            pounds == 1000
            # object. not an int
