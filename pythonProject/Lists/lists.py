employees = ['Hamada', 'Amira', 'Yassin', 'Frida']
print(employees[0])
print(employees[1])
print(employees[2])
print(employees[-1]) # if we don't know the length of the list we can use -1 to get the last index
print(employees[-3]) # counting from the back to forward, last index would be -1 and before the last one would be -2 etc
# print(employees[50]) # index out of range
# only print 'Amira', 'Yassin'
print(employees[1:3]) # starts at 1 and ends at 3
print(employees[:3]) # starts with index 0
print(employees[1:]) # starts with index 1 but ends at the end of the index
print(employees[0:2:1]) # start at index 1 and end at index 2 but step by step
print(employees[::1]) # no start no end but step by step
print(employees[::2]) # no start no end but two steps at a time and so on
print('___________________________________________________')
print(employees)
employees[0] = 'Mohamed' # to change a string in a list
print(employees)
employees[-1] = 'Frida Mohamad' # -1 to get the last index of the list
print(employees)
employees[2] = 'Yassin Mohamad'
print(employees)
employees[1] = 'Amira Abdalla'
print(employees)
employees[0] = 'Mohamed Farahat' # choosing the index in the list and replacing the value
print(employees) # then print it
print('___________________________________________________')
employees[0:2] = 'Mohamed Mohamad Farahat', 'Amira Ahmed Abdalla'
print(employees)
employees[0:2] = '' # that would remove the first and the second index from the list
print(employees)
print('___________________________________________________')
# for loop
employees = ['Hamada', 'Amira', 'Yassin', 'Frida']
for i in range(4):
    print(employees[i])
    print(i)

for i in range(len(employees)):
    print(employees[i])

for i in range(len(employees)):
    print(f'index {i} in employees is: {employees[i]}')
print('___________________________________________________')
# enumerate
for index, item in enumerate(employees):
    print(f'index {index} in employees is {item}')
print('___________________________________________________')
# in and not in
# print('Hamada' in employees) # true
# print('Amira' in employees) # true
# print('Mohamed' in employees) # false

# print('Hamada' not in employees) # false because Hamada is in employees
# print('_________________________________________________')

# print('Name of the employee: ')
# name = input()
# if name not in employees:
#     print('There is no employee with that name ' + name)
# else:
#     print(f'The employee name is {name}')
print('____________________________________________________')
# random.choice() and random.shuffle()
import random
employees = ['Hamada', 'Amira', 'Yassin', 'Frida']
print(random.choice(employees))
print(random.choice(employees))
print(random.choice(employees))
(random.shuffle(employees))
print(employees)
