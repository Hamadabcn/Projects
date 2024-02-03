#upper()
print('hamada'.upper())
test = 'Hello, world!'
print(test.upper())
print('_____________________________________________')
#lower()
print('HAMADA'.lower())
test = 'HELLO, WORLD!'
print(test.lower())
'''
print('_____________________________________________')
print('How are you')
feeling = input()
if feeling.lower() == 'great': # lower makes sure all the letters are small because python is letter sensitive
    print('I also feel great today')
else:
    print('Hopefully the rest of you day is good')
print('_____________________________________________')
'''
# islower and isupper
test = 'HELLO, WORLD!'
print(test.islower()) # islower makes sure no capital letters are in the string returns a boolean value
print(test.isupper()) # isupper makes sure all the letters are capital letters in the string
print('______________________________________________')
# title()
print('HAMADA'.title())
txt = 'Welcome to my 2nd world'
print(txt.title()) # capitalizes all the first letters of every word
print('______________________________________________')
# capitalize
print('hAMADA'.capitalize()) # changes the first letter of the string to capital letter and the rest to small letter
print('______________________________________________')
# swapcase()
print('hamada'.swapcase()) # swaps the letters if capital to small and if small to capital
txt = 'Hello My Name Is Hamada'
print(txt.swapcase())



