"""This is a first homework on Python"""
# the first task
firstNumber = int(input("Enter a first number"))
secondNumber = int(input("Enter a second number"))
thirdNumber = int(input("Enter a third number"))
userChoose = int(input("What do you want to do? Enter 1 if you want to multiply your number. Enter 2 if you want to add your numbers."))
if userChoose == 1:
    print(f"You multiple {firstNumber}, {secondNumber}, {thirdNumber} and result is", firstNumber * secondNumber * thirdNumber)
elif userChoose == 2:
    print(f"You add {firstNumber}, {secondNumber}, {thirdNumber} and result is", firstNumber + secondNumber + thirdNumber)
else:
    print("Sorry, I can't help you, but have a nice day!")
