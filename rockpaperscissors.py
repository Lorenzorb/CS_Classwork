from random import randint
import sys
import time



while True:


    value = randint(1,3)

    choice = int(input('Please enter\n 1 for rock\n 2 for paper or\n 3 for scissors\n '))
    print(choice)

    if choice == 1:
        print('you picked rock')
    elif choice == 2:
        print('you picked paper')
    elif choice == 3:
        print('you picked scissors')
    else:
        print('ehhh i think you aren\'t understanding me')
        for i in range(3):
            time.sleep(.5)
        continue
        

    for i in range(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(.5)


    if value == 1:
        print('your opponent picked rock')
    elif value == 2:
        print('your opponent picked paper')
    elif value == 3:
        print('your opponent picked scissors')
    else:
        print('ah fuck i give up')

    if choice == value:
        print('DRAW')
    elif value == 1 and choice == 3:
        print('YOU LOSE')
    elif value == 3 and choice == 1:
        print('YOU WIN')
    elif choice > value:
        print('YOU WIN')
    else:
        print('YOU LOSE')

    while True:
        answer = input('Do you want to play again? y/n? ')
        if answer in ('y , n'):
            break
        print('invalid input')
    if answer == 'y':
        continue
    else:
        print('well fine then...')
        break