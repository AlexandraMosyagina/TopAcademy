# the first task

# check cast to int
while True:
    try:
        userNumber = int(input("Please, enter a number in the range from 1 to 100.\n"))
        break
    except:
        print("Please, enter a number.")
        continue

"""two if because in the task the program should print fizz buzz when a number multiple 3 and 5 at the same time.
but if I do it another if the program also print the first if too and if I do it another elif the program doesn't print anything at all."""
if userNumber % 3 == 0 and userNumber >= 1 and userNumber <= 100:  # check multiple to 3 and range
    print("Fizz")
if userNumber % 5 == 0 and userNumber >= 1 and userNumber <= 100:  # check multiple to 5 and range
    print("Buzz")
elif userNumber % 3 != 0 and userNumber % 5 != 0:  # if a number doesn't multiple 3 and 5
    print(f"{userNumber}")
elif userNumber < 1 or userNumber > 100:  # error message
    print(f"Number {userNumber} isn't in the range from 1 to 100.")
