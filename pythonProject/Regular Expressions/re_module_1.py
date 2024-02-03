import re

# search
txt = 'My name is Hamada'
search = re.search("[A-Z]", txt)
print(search)
print(search.span())
print(dir(search))
print(search.group())
print('_______________________________________________')

test = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office"
search = re.search(r"\d{3}-\d{3}-\d{4}", test)
print(search)
print(search.group())
print(search.string)