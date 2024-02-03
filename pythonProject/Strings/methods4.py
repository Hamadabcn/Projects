# rjust(), ljust(), center()
test = 'Hello'
print(test.rjust(10))
print(test.ljust(10))
print(test.center(20))

print(test.center(11, '#')) # 11 to get the same amount of hastags on each side
print(test.rjust(10, '#'))
print(test.ljust(10, '#'))
print('_______________________________________________________')
# expandtabs()
test = 'Hello \thow are you? \tthanks I am fine'
print(test)
print(test.expandtabs(1)) # reduces whitespaces
print(test.expandtabs(10)) # increases whitespaces