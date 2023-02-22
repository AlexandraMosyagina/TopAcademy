# this game allows duplicates of numbers
import random

# generate random number
generate = random.randint(1000, 9999)
number = [int(i) for i in str(generate)]
print(number)

# set the status of game
game = False
# ask for a number for the first time
generateUser = random.randint(1000, 9999)
numberUser = [int(i) for i in str(generateUser)]
print(numberUser)

# set the counters
cows = 0
bulls = 0


# check for bulls and cows
def countBullsAndCows(position):
    global bulls, cows
    while position != 4:
        # check for bulls
        if number[position] == numberUser[position]:
            bulls += 1
        # check for cows
        elif numberUser[position] in number:
            cows += 1
        return countBullsAndCows(position + 1)
    # print the results
    print(f"In your number {bulls} bulls and {cows} cows.\n")
    # reset the results
    cows = 0
    bulls = 0


def bullsAndCows(a, b):
    global game
    global numberUser
    global number
    while game == False:
        # check for win
        if numberUser == number:
            print("You're win!")
            game = True
        else:
            # count the results
            countBullsAndCows(0)
            # ask for a number
            generateUser = random.randint(1000, 9999)
            numberUser = [int(i) for i in str(generateUser)]
            print(numberUser)


bullsAndCows(cows, bulls)
