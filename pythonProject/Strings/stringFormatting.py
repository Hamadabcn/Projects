name = 'Hamada'
age = 42 # you can convert this to a string '' or you can add string to the age
print('Hello, my name is '+name+' and my age is '+str(age) + ' years old. I am still young and productive')
print('My name is %s. I am %d years old' % (name, age))
print("_____________________________________________")
rank = 9.0
print(rank)
print('My name is %s. I am %d years old. And my rank is %.2f' % (name, age, rank))
print('_____________________%_______________________')
first_name = 'Mohamed'
last_name = 'Farahat'
age = 42
profession = 'Programmer'
affiliation = 'Microsoft'
print('Hello, %s %s. You are %s. You are %s You were a member of %s.' % (first_name, last_name, age, profession, affiliation))
print('_________________str.format__________________')
print('My name is {}. I am {} years old.'.format(name, age))
print('My name is {:s}. I am {:d} years old, and my rank is {:.3f}'.format(name, age, rank))
print('My name is {1}. I am {0} years old.'.format(age, name)) # indexing so he changes them round
print('My name is {name_key}. I am {age_key} years old.'.format(age_key=age, name_key=name))
print('_________________f.strings___________________')
print(f'My name is {name}. I am {age} years old')
print(f'My name is {name}, and my age next year will be {age+1} years old')
print(f'My name is {name}, and last year I was {age-1} years old')
