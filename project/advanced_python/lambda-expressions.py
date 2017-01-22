

l = lambda x: x > 5
# l is a func that takes x as a parameter
# and return if x > 5

# Same as:
# def l(x)
#    return x > 5

print(l(10))

# takes in a list
# filters it based on the func check result
def alter(values, check):
    # return list(filter(check, values))
    # filter would the same as the list comprehension below
    return [val for val in values if check(val)]

my_list = [1,2,3,4,5]
another_list = alter(my_list, lambda x: x != 5)
# pass in lambda expr as a check parameter

print(another_list)

def check_not_five(x):
    return x != 5

another_list2 = alter(my_list, check_not_five) # method here without brackets!

print(another_list2)

def remover_number(values):
    return alter(values, lambda x: x not in [str(n) for n in range(10)])
    # if x is not a number then False

print(remover_number("hel5lo"))

def skip_letter(values, letter):
    return alter(values, lambda x: x != letter)

print(skip_letter("hello", 'e'))

