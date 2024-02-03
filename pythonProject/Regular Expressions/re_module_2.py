import re

# sub() can replace items in a string
string = """Hello my number is 415-555-9999 and
my friend's phone number is 415-666-8888"""

replace = re.sub(r'\d{3}-\d{3}-\d{4}', '630 379 4840', string, 1)  # takes 4 variables
print(replace)
print('__________________________________________')

txt = 'I am a student at Hsoub Academy'
replace = re.sub(r'\s', '-', txt)  # if you don't indicate a count it will replace all the spaces with '-'
print(replace)
# now what if we want to put a '-' only between Hsoub-Academy
replace = re.sub(r'Hsoub Academy', 'Hsoub-Academy', txt, 1)
print(replace)
print('__________________________________________')

# split cuts the string into pieces
txt = 'I am a student at Hsoub Academy'
search = re.split(r'\s', txt)  # notice how it splits the string into a list of strings
print(search)
search = re.split(r'\s', txt, 4)
print(search)
print('___________________________________________')

# practice
# this is how I did it using sub()
txt = 'I-am-a-student-at-Hsoub-Academy'
replace = re.sub(r'I-am-a-student-at-Hsoub-Academy', 'I am a student at Hsoub Academy', txt)
print(replace)
print('___________________________________________')
# this how the teacher did it
# this is done using sub()
search_one = re.sub("-", " ", txt)
print(search_one)
print('___________________________________________')
# doing the same thing as above but using split()
search_two = re.split(r'-', txt)
print(search_two)
print(" ".join(search_two))
