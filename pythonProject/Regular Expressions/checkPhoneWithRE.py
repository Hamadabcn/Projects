import re


def isPhoneNumber(text):
    is_phone = re.search(r'\d{3}-\d{3}-\d{4}', text)

    if is_phone:
        print(f'the {text} is a valid phone number.')
    else:
        print(f'the {text} is not a valid phone number.')


print('Is 415-555-4242 a phone number?')
isPhoneNumber('415-555-4242')  # this will return true because it is the right sequence of phone number
print('Is hello a phone number')
isPhoneNumber('hello')   # this will return false because 'hello' is not a phone number
print('_______________________________________')

# findall() this works the same as search but the difference is in the return
# search() returns an object and only returns the first result and if the search is false it returns none
# but findall() returns a list with all the identical values and if the search is false it returns an empty list

string = """Hello my number is 415-555-9999 and
my friend's phone number is 415-666-8888"""
search = re.findall(r"\d{3}-\d{3}-\d{4}", string)  # notice how findall() returns a list
print(search)

test_search = re.findall(r"A", string)
print(test_search)  # notice how this will return an empty list because there are no capital 'A' in the string
print('_______________________________________')

# practice
phone_number = input('Please Enter your Phone number: ')
search_phone = re.findall(r'\d{3}-\d{3}-\d{4}', phone_number)

list = []

if search_phone == []:
    print('This phone number is not valid')
else:
    list.append(search_phone)
    print('The phone number is added')

