import random

level = 0
count = 0
print("Hello lets play a game")

game = True
while True:
    print("To begin please select a level of difficulty")
    level = int(input("input a level of difficulty 1 for easy, 2 for medium and 3 for hard!.\n"))
    if level == 1:
        print("This is the easy level")
        break
    if level == 2:
        print("This is the medium level")
        break
    if level == 3:
        print("This is the hard level")
        break
    elif level != 1 and level != 2 and level != 3:
        print("invalid input!")

while level == 1:
    easy = random.randint(1, 10)
    try:
        print("I've got a private number between 1 and 10, are you able to guess it?")
        attempts = 6
        for attempt in range(attempts, 0, -1):
            print("You have {0} attempts left.".format(attempt))
            userNumber = int(input("please enter number guessed \n"))
            if userNumber > easy:
                print("That was wrong, your answer is too high")
            elif userNumber < easy:
                print("That was wrong, Your answer is too low")
            else:
                print("You got it right")
                break
            attempts -= 1
            if attempts <= 0:
                print("Game Over")
                break
    except ValueError:
        print("please input a number")

while level == 2:
    medium = random.randint(1, 20)
    try:
        print("I've got a private number between 1 and 20, are you able to guess it?")
        attempts = 4

        while True:
            userNumber = int(input(f'You have {attempts} attempts.\nGuess the number between 1 and 20!.\n'))
            if userNumber == medium:
                print(f'You got it right and still had{attempts}attempts left!.')
                break
            elif userNumber > medium:
                print("You are wrong, your answer is Too high")
            elif userNumber < medium:
                print("You are wrong your answer is Too low")

            attempts -= 1
            if attempts <= 0:
                print("Game Over")
                break
    except ValueError:
        print("Please input a number")

while level == 3:
    hard = random.randint(1, 50)
    try:
        print("I've got a private number between 1 and 50, are you able to guess it")
        attempts = 3
        for attempt in range(attempts, 0, -1):
            print("You have {0} attempts left.".format(attempt))
            userNumber = int(input("please enter number guessed \n"))
            if userNumber > hard:
                print("That was wrong, your answer is too high")
            elif userNumber < hard:
                print("That was wrong, your answer is too low")
            else:
                print("You got it right")
                break
            attempts -= 1
            if attempts <= 0:
                print("Game Over")
    except ValueError:
        print("please input a number")

again = str(input("Would you like to play again? Yes or No"))
if again == "No":
    game = False
else:
    game = True
    count = count + 1
quit()
