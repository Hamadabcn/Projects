# index
employees = ['Hamada', 'Hamada', 'Amira', 'Yassin', 'Frida']
print(employees.index('Amira')) # return 1 when true
# print(employees.index('Mohamed')) # ValueError: 'Mohamed' is not in list
print('_____________________________________________________')
# count
print(employees.count('Hamada'))
print(employees.count('Amira'))
print('_____________________________________________________')
# copy
test = employees.copy()
print(employees)
print(test)
print('_____________________________________________________')
# clear
employees.clear() # clears all the list of employees
print(employees)