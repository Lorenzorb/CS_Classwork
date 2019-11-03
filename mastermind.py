import random

print('this is a game called mastermind.\n')
print('the computer will choose 4 random numbers between 1 and 9 and you just have to guess them in order!\n')
print('when it asks for your input, type any number between 1 and 9 simple as that\n')
print('The computer will tell you how many numbers are correct! \n you\'ll get ten chances so good luck!\n')


from random import randint
while True:
    n1 = randint(1,9)
    n2 = randint(1,9)
    n3 = randint(1,9)
    n4 = randint(1,9)
    c = 1

    #remove the hash symbol to see the correct answer during gameplay#
    #print (n1,n2,n3,n4)#


    guess1 = input("guess the first number: ")
    guess2 = input("guess the second number: ")
    guess3 = input("guess the third number: ")
    guess4 = input("guess the fourth number: ")
    guess1 = int(guess1)
    guess2 = int(guess2)
    guess3 = int(guess3)
    guess4 = int(guess4)
    numberswrong = 0

    if guess1 != n1:
        numberswrong += 1
    if guess2 != n2:
        numberswrong += 1

    if guess3 != n3:
        numberswrong += 1

    if guess4 != n4:
        numberswrong += 1

    if numberswrong == 0:
        print('Well Done!')
        print('It took you ' + str(c) + ' tries to guess the number!')
        answer = input("would you like to play again? y/n ")
        if answer == 'n':
            break
        if answer == 'y':
            continue

    else:
        print('You got ' + str(4-numberswrong) + ' numbers right.')
    c += 1