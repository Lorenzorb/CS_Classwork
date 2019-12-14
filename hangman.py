
print("Guess the letters for the word. you have 7 tries\nHint: try brands of car")

WORD = list("ford")
DISPLAY = []
GUESSED = []
DISPLAY = ["?"] * len(WORD)

guesses = 0
while guesses < 7:
    print("Word to guess:", DISPLAY)
    print(guesses)
    print("Wrongly gussed letters:",GUESSED)
    if WORD == DISPLAY:
        print("Good Job!")
        break
    char = input("Please guess a letter!")
    if WORD.__contains__(char):
        for check, num in zip(WORD,range(len(WORD))):
            if check == char:
                DISPLAY[num] = char
    else:
        if GUESSED.__contains__(char):
            print("You already tried that one!")
        else:
            guesses += 1
            GUESSED.append(char)
else:
    print("You lose\nThe word was: ", WORD)