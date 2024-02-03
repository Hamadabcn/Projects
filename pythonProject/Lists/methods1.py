# append and insert
employees = ['Hamada', 'Amira', 'Yassin', 'Frida']
employees.append('Tom') # append will add the new employee to the end of the list
print(employees)
employees.append('Juan')
print(employees)

employees.insert(1, 'Carlos') # insert add the new value to a specific part of the list
print(employees)

employees.insert(0, 'Eman')
print(employees)

employees.insert(2, 'Mohamed')
print(employees)

oldEmployees = ['Mahmoud', 'Walla'] # a list inside a list
employees.append(oldEmployees)
print(employees)
print(employees[9][0])
print('____________________________________________________________')
# extend
employees = ['Hamada', 'Amira', 'Yassin', 'Frida']
oldEmployees = ['Mahmoud', 'Walla']
employees.extend(oldEmployees) # extend adds the values to the main list not as above a list inside a list
print(employees)
print('____________________________________________________________')
# remove
employees.remove('Walla') # removes a key from the list
print(employees)

# employees.remove('Carlos')
# print(employees) # x not in list

employees = ['Hamada', 'Hamada', 'Amira', 'Yassin', 'Frida']
employees.remove('Hamada') # it will always remove the first string in the list
print(employees)
print('____________________________________________________________')
# del statement if you know the index you want to remove this is a better practice
del employees[0] # deletes the index indicated
print(employees)
print('____________________________________________________________')
# sort
numbers = [2, 5, 3.14, 1, -7 ]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
employees.sort(reverse=True)
print(employees)
employees.sort()
print(employees)

# spam = [1, 3, 2, 4, 'Hamada', 'Amira'] # not supported between instances of 'str' and 'int'
# spam.sort()
# print(spam)
print('____________________________________________________________')
# reverse
employees = ['Hamada', 'Amira', 'Yassin', 'Frida']
employees.reverse() # reverses the order of the list
print(employees)