# the second task

# check cast to int
while True:
    try:
        userNumber = int(input("Please, enter a number.\n"))
        userPower = int(input("Please, enter a power in the range of 0 to 7.\n"))
        break
    except:
        print("Please, enter a number.")
        continue

if userPower < 0 or userPower > 7:  # check a range of the power
    print("The power isn't in the range of 0 to 7.")
else:  # raise a number to a power
    print(userNumber ** userPower)
