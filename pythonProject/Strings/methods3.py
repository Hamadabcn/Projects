#join
list = ['Hello', 'world', 'here I come', 'are you ready', '!!!']
print(' '.join(list)) # adds what ever you want between the space
print('-'.join(list))
print('_'.join(list))
print('#'.join(list))
print('ABC'.join(list))
print('_________________________________________________')
# split
test = 'Hello, world here I come are you ready !!!'
print(test.split(' ')) # splits all the string into a list of strings
test = 'MyABCnameABCisABCHamada'
print(test.split('ABC')) # splits what ever you want from the string
test = '''Hello
how are you?
thanks I am fine'''
print(test.split('\n'))
print('__________________________________________________')
# splitlines
test = '''Hello
how are you?
thanks I am fine'''
print(test.splitlines())
test = 'Hello\nhow are you?\nthanks I am fine'
print(test.splitlines())