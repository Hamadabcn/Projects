# startswith and endswith
test = 'Hello, world'
print(test.startswith('Hello')) # makes sure the string starts with that word
print(test.endswith('world!')) # makes sure the string ends with that word even with the exclamation mark (stupid)
print(test.startswith('H')) # checks if the string starts with capital 'H'
print(test.endswith('d'))
print(test.startswith('w', 7, 11))
print('______________________________________________')
# strip, rstrip, lstrip # right strip and left strip
test = '                     Hello, World                        '
print(test)
print(test.strip()) # strips all the whitespaces left and right
print(test.lstrip())
print(test.rstrip())

test = ('@@@Hello, World@@@')
print(test)
print(test.strip('@')) # strips all the whitespaces left and right
print(test.lstrip('@'))
print(test.rstrip('@'))

test = ('@#@#@#Hello, world@#@#@#')
print(test)
print(test.strip('@#@#')) # strips all the whitespaces left and right
print(test.lstrip('@#@#'))
print(test.rstrip('@#@#'))
print('___________________________________________________')
#zfill
hours = '1'
min = '1'
seconds = '1'
print(f'The time is {hours} hours and {min} minutes and {seconds} seconds')
print(f'{hours}:{min}:{seconds}')
print(f'{hours.zfill(2)}:{min.zfill(2)}:{seconds.zfill(2)}') # adds the double digits to the hours
print(f'{hours.zfill(3)}:{min.zfill(3)}:{seconds.zfill(3)}')

