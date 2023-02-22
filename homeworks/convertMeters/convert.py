"""This is a first homework on Python."""
# the third task
userNumber = int(input("Enter the number of meters."))
userChoose = int(input("What do you want to do? Enter 1 if you want to convert meters to miles. Enter 2 if you want to convert meters to inches. Enter 3 if you want to convert meters to yards."))
if userChoose == 1:
    print(f"In {userNumber} meters", userNumber / 1609.34, "miles")
elif userChoose == 2:
    print(f"In {userNumber} meters", userNumber * 39.37, "inches")
elif userChoose == 3:
    print(f"In {userNumber} meters", userNumber * 1.094, "yards")
else:
    print("Sorry, I can't help you, but have a nice day!")