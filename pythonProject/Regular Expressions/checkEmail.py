import re


def isEmail(email):
    is_email = re.search(r'^[A-z0-9]+[\.-]?[A-z0-9]+@\w+\.\w{2,3}$', email)

    if is_email:
        print(f'the {email} is a valid email')

    else:
        print(f'the {email} is not a valid email')


print('Is hsoub.academy@gmail.com a email?')
isEmail('hsoub.academy@gmail.com')
print('Is hsoub.academy@gmail a email')
isEmail('hsoub.academy@gmail')
