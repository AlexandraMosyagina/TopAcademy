import string

# the second task
userStringCount = input("Please, enter something\n")
letters = string.ascii_letters
numbers = string.digits
counterLetters = 0
counterNumbers = 0

for i in userStringCount:
    for j in letters:
        if i == j:
            counterLetters += 1

for i in userStringCount:
    for j in numbers:
        if i == j:
            counterNumbers += 1

print(f"In your string {counterNumbers} numbers and {counterLetters} letters")
