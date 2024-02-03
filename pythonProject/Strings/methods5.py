# index(substring, start, end)
test = 'Hello, world'
print(test.index('world')) # find the position of the letter in the string index 0
print(test.index('e')) # you can also search for a single letter index 0
# print(test.index('world', 0, 4)) error substring not found
try:
    print(test.index('world', 0, 4))
except ValueError:
    print('String not found')
print('___________________________________________________')
# find(substring, start, end)
test = 'Hello, world'
print(test.find('world')) # works as index
print(test.find('world', 0, 4)) # returns -1 string not found
print('___________________________________________________-')
# replace(old value, new value, count)
text = 'one plus one equals two'
print(text.replace('one', '1')) # replaced the word one with number 1
print(text.replace('one', '1', 1)) # how many times you want to count

