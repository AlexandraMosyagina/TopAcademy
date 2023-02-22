#the task fourth

# check cast to int
while True:
    try:
        salesOne = int(input("Please, enter a level of sales of the first manager.\n"))
        salesTwo = int(input("Please, enter a level of sales of the second manager.\n"))
        salesThree = int(input("Please, enter a level of sales of the third manager.\n"))
        break
    except:
        print("Please, enter numbers.")
        continue

# count for 1 manager
if salesOne < 500:
    salaryOne = 200 + (salesOne / 100 * 3)
elif salesOne >= 500 and salesOne <= 1000:
    salaryOne = 200 + (salesOne / 100 * 5)
elif salesOne > 1000:
    salaryOne = 200 + (salesOne / 100 * 8)

# count for 2 manager
if salesTwo < 500:
    salaryTwo = 200 + (salesTwo / 100 * 3)
elif salesTwo >= 500 and salesTwo <= 1000:
    salaryTwo = 200 + (salesTwo / 100 * 5)
elif salesTwo > 1000:
    salaryTwo = 200 + (salesTwo / 100 * 8)

# count for 3 manager
if salesThree < 500:
    salaryThree = 200 + (salesThree / 100 * 3)
elif salesThree >= 500 and salesThree <= 1000:
    salaryThree = 200 + (salesThree / 100 * 5)
elif salesThree > 1000:
    salaryThree = 200 + (salesThree / 100 * 8)

# the best manager
if salesOne > salesTwo and salesOne > salesThree:
    salaryOne += 200
    best = "first"
elif salesTwo > salesOne and salesTwo > salesThree:
    salaryTwo += 200
    best = "second"
elif salesThree > salesOne and salesThree > salesTwo:
    salaryThree += 200
    best = "third"

print(f"The salary of the first manager is {salaryOne}.\nThe salary of the second manager is {salaryTwo}.\nThe salary of the third manager is {salaryThree}.\nThe best manager is {best}.")


