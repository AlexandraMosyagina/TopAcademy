# the fourth task

userString = input("Please, enter something\n")
userWord = input("Please, enter the word for search\n")
counterWords = 0

for i in range(len(userString)):
    if userString[i:i + len(userWord)] == userWord:
        counterWords += 1

print(f"In your string {counterWords} '{userWord}'")
