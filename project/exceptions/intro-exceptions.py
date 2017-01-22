import requests
from json import  JSONDecodeError

# number = input("Enter a number")
# try:
#     print(int(number) * 2)
# except ValueError:
#     print("Didn't enter a number")
# except LookupError:
#     print("This should never happen")

r = requests.post('http://text-processing.com/api/sentiment',
                  data={'text':'hello world'})
try:
    label = r.json()['label']
    print(label)
except JSONDecodeError:
    print("Can't decode")
except KeyError:
    print("We got JSON back but it didn't have a key")

