# dictionaries
hamada = {
    'name': 'Mohamed Farahat',
    'date of birth': '23-09-1981',
    'salary': 5500,
    'phone number': '630379484',
    'address': 'muntaner 183',
    'in the company since': '2004',
    'skills': ['python', 'javascript', 'html', 'css']
}
print(hamada)
print(hamada['name'])
print(hamada['date of birth'])
print(hamada['skills'][0])  # this prints a specific key of the dictionary
print(hamada['in the company since'])
print('__________________________________________________________')

list = ['cats', 'dogs', 'moose']
myList = ['dogs', 'moose', 'cats']
print(list == myList)  # this will return false because both dictionaries are not equal
print(list[0])
print(myList[0])  # that is why it returns false because it is a list
print('__________________________________________________________')
# that exercise just came to me. I sorted the lists first then asked if they were equal and returned true
print(list.sort() == myList.sort())  # this way it is going to sort both dictionaries and it will return true
print(list)
print(myList)
print('__________________________________________________________')
dictionary = {'name': 'Max', 'species': 'dog', 'age': '8'}
myDictionary = {'species': 'dog', 'age': '8', 'name': 'Max'}
print(dictionary == myDictionary)  # this will return true on the contrary to list because it's a dictionary
print(dictionary['age'])
print(myDictionary['age'])
print('__________________________________________________________')
# a simple birthday agenda written in python
# birthdays = {'Hamada': 'September 23rd.', 'Amira': 'January 01st.', 'Yassin': 'July 05th.', 'Frida': 'July 31st.'}
# while True:   # an infinite loop
#     print('Enter a name: (blank to quit) ')
#     name = input()
#     if name == '':
#         break
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name + ' happy birthday 🎂 ' + name)
#     else:
#         print('I don\'t have information for ' + name)
#         print('What is their birthday? ')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated. ')
print('__________________________________________________________')
hamada = {
    'name': 'Mohamed Farahat',
    'date of birth': '23-09-1981',
    'salary': 5500,
    'phone number': '630379484',
    'address': 'muntaner 183',
    'in the company since': '2004',
    'skills': ['python', 'javascript', 'html', 'css']
}
print(hamada.keys())  # prints only the keys (name, date of birth, salary, etc.)
print(hamada.values())  # prints only the values (Mohamed Farahat, 23-09-1981, 5500, etc.)
print(hamada.items())  # prints both the keys and the values of the dictionary into a tuples
print('___________________________________________________________')
# two-dimensional dictionaries which means dictionary inside a dictionary
amira = {
    'frontend': {
        1: 'HTML',
        2: 'CSS',
        3: 'Javascript'
    },
    'backend': {
        1: 'Python',
        2: 'Node.js',
        3: 'Next.js'
    }
}
print(amira)
print(amira['frontend'])
print(amira['frontend'][3])
print(amira['backend'])
print(amira['backend'][1])
