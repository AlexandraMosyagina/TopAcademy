import random

# store steps of players
humanSteps = []
computerSteps = []

# cross or zero
cross = "X"
zero = "O"

# game status
status = True

# write win combination
winCombination = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


# display board
def printBoard(cell):
    print("     ┆     ┆")
    print("  {}  |  {}  |  {}".format(cell[1], cell[2], cell[3]))
    print('_____┆_____┆_____')

    print("     ┆     ┆")
    print("  {}  |  {}  |  {}".format(cell[4], cell[5], cell[6]))
    print('_____┆_____┆_____')

    print("     ┆     ┆")

    print("  {}  ┆  {}  ┆  {}".format(cell[7], cell[8], cell[9]))
    print("     ┆     ┆")


def game():
    global status, cell
    # generate a board for the first time
    firstGeneration = 0
    if firstGeneration == 0:
        cell = [' ' for i in range(10)]
        firstGeneration += 1
        printBoard(cell)
    # start the game
    while status == True:
        # ask player for move and cast input to int
        humanMove = int(input("Please, do your move."))
        # check if position is already in use
        if cell[humanMove] != ' ':
            # ask another move while there is an empty cell
            while cell[humanMove] != ' ':
               humanMove = int(input("This cell isn't empty. Please, do your move again."))
        print(f"Your move is {humanMove}")
        # write player's move in steps
        humanSteps.append(humanMove)
        # print player's move
        cell[humanMove] = cross
        printBoard(cell)
        # check for player's win
        for i in winCombination:
            if all(j in humanSteps for j in i):
                print("Player is win!")
                status = False
                return status
        # check for draw
        if len(humanSteps) + len(computerSteps) == 9:
            print("Draw!")
            status = False
            return status
        # use random for computer move
        computerMove = random.randrange(1, 10)
        # check if position is already in use
        if cell[computerMove] != ' ':
            # generate another move while there is an empty cell
            while cell[computerMove] != ' ':
                computerMove = random.randrange(1, 9)
        # write computer's move in steps
        computerSteps.append(computerMove)
        print(f"Computer's move is {computerMove}")
        # print computer's move
        cell[computerMove] = zero
        printBoard(cell)
        # check for computer's win
        for i in winCombination:
            if all(j in computerSteps for j in i):
                print("Computer is win!")
                status = False
                return status
        print(humanSteps)
        print(computerSteps)


game()
