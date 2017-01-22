# create custom exceptions

class MissingLabelError(KeyError): # subcalss a certain error
    pass

class PageNotFoundError(LookupError):
    pass

class IncorrectPasswordError(ValueError):
    pass

class IncorrectUsernameError(ValueError):
    pass

class APIThrottleLimitError(RuntimeError):
    pass


# Usage
def login():
    # Case 1
    raise IncorrectUsernameError # raise errors
    # Case 2
    # raise IncorrectPasswordError

# Raise different errors for different cases

try:
    login()
except IncorrectUsernameError:
    print("Your username was incorrect")
except IncorrectPasswordError:
    print("Your password was incorrect")