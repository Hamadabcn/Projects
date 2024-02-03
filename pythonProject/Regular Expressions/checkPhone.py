# 415-555-1234

def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):  # always one more because the 0 indexing
        if not text[i].isdecimal():
            return False

    return True


print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))  # this will return true because it is the right sequence of phone number
print('Is hello a phone number')
print(isPhoneNumber('hello'))  # this will return false because 'hello' is not a phone number
