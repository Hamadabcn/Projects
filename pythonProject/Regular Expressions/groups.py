# groups
import re
phone = '415-555-9999'
search = re.search(r"(\d{3})-(\d{3}-\d{4})", phone)
print(search.group())
print(search.group(0))
print(search.group(1))
print(search.group(2))
print('_____________________________________')

date = '01-01-1983'
search = re.search(r"(\d{2})-(\d{2})-(\d{4})", date)
print(search.group(0))
day = search.group(1)
month = search.group(2)
year = search.group(3)
print(f'You were born in the {day}st of the {month}th of the year {year}, you are a legend')
print('_____________________________________')
(day, month, year) = search.groups()
print(f'You were born in the {day}st of the {month}th of the year {year}, you are a legend')

