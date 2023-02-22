list1 = [14, 5, 2, 19, 32, 12, 111, 5, 2, 6]
list2 = [52, 1, 111, 20, 32, 10, 7, 1, 20, 142]

# the first task
listSum = list1 + list2
print(listSum)

# the second task
temp1 = []
temp2 = []
for i in list1:
    if i not in temp1:
        temp1.append(i)
for j in list2:
    if j not in temp2:
        temp2.append(j)
withoutDuplicates = temp1 + temp2
print(withoutDuplicates)

# the third task
duplicates = []
for i in list1:
    for j in list2:
        if i == j:
            duplicates.append(i)
            break
print(duplicates)

# the fourth task
uniqElements = list(set(list1 + list2))
print(uniqElements)

# the fifth task
max1 = max(list1)
max2 = max(list2)
maxLists = [max1, max2]
print(maxLists)
