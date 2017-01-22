# def divide_secure(number, divisor):
#     if divisor == 0:
#         raise ValueError("The divisor is 0")
#     return number/divisor


def divide_secure(number, divisor):
    assert divisor != 0, 'Divided a number by zero' # Error message
    return number/divisor

# assertions can be turned off


