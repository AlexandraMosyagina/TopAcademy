# the third task
userString = input("Please, enter something\n")
userSymbol = input("Please, enter the symbol for search\n")
counterSymbols = 0

for i in userString:
        if i == userSymbol:
            counterSymbols += 1

print(f"In your string {counterSymbols} '{userSymbol}'")
