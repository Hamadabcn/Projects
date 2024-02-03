# get look for a specific information in the dictionary
hamada = {
    'name': 'Mohamed Farahat',
    'date of birth': '23-09-1981',
    #'salary': 5500,
    'phone number': '630379484',
    'address': 'muntaner 183',
    'in the company since': '2004',
    'skills': ['Python', 'Javascript', 'HTML', 'CSS']
}
# print(hamada['name'] + ' receives a salary of ' + str(hamada['salary']))
print(hamada['name'] + ' receives a salary of ' + str(hamada.get('salary', 'no salary')))
print('_____________________________________________________')
# setdefault adds new information that was not in the dictionary
print(hamada)
print(hamada.setdefault('name', 'amira'))
print(hamada)
print(hamada.setdefault('salary', 2000))
print(hamada)

if 'language' not in hamada:
    hamada['language'] = 'CSS'
print(hamada)
print('______________________________________________________')
# update the keys in the dictionary
numbers = {1: 'four', 2: 'three', 3: 'two', 4: 'five', 5: 'six'}
print(numbers)
numbers.update({1: 'one'})
numbers.update({2: 'two'})
numbers.update({3: 'three'})
numbers.update({4: 'four'})
numbers.update({5: 'five'})
print(numbers)
numbers.update({6: 'six'})  # adds a new value and key to the dictionary
numbers.update({7: 'seven'})
print(numbers)
print('______________________________________________________')
# clear
print(hamada)
hamada.clear()  # clear empties all the values and the keys from the dictionary
print(hamada)
