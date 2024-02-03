import random

name = input('What is your name? : ')

print('Good Luck, and always have fun! ' + name)

names = ['hamada', 'amira', 'yassin', 'frida', 'eman', 'mahmoud', 'jane', 'adam', 'ahmed', 'juan']

word = random.choice(names)

print('The name is:')

guesses = ' '

turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1

    if failed == 0:
        print('YOU WIN!')
        print('The name is:', word)
        break

    guess = input('Guess a Character: ')
    guesses += guess   # be careful guesses += guess

    if guess not in word:
        turns -= 1
        print('Wrong Guess, Good luck next time!')
        print('You have,', + turns, 'more guesses')

        if turns == 0:
            print('You lose')
