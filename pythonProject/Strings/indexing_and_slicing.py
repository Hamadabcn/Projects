stringOne = "This is string one"
print(stringOne[-4])
print("------------------------")
#strings [start:end:step]
print(stringOne[5:14]) # this slices the part of the sentence by indexing
print(stringOne[:13]) # index 0 and counting
print(stringOne[0:]) # that would be the whole string
print(stringOne[:]) # that would also be the whole string
print(stringOne[:-4]) #
print(stringOne[4:14]) # this print the slice of the string 'is string
print(stringOne[-13:-4]) # this also print 'is string'
print("------------------------")
#steps
print(stringOne[0:17:1])
print(stringOne[:-10]) # this selects how much of the string you need (index 1)
print(stringOne[::1])
print(stringOne[::2])
print(stringOne[::-1]) # wow that is cool
