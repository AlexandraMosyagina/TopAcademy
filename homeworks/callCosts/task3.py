# the third task
# check cast to int
while True:
    try:
        userChoiceSelf = int(input("Please, enter your mobile operator.\n 1 - Megafon, 2 - Beeline, 3 - MTS, 4 - Tele2\n"))
        userChoiceInter = int(input("Please, enter interlocutor's mobile operator.\n 1 - Megafon, 2 - Beeline, 3 - MTS, 4 - Tele2\n"))
        userChoiceCost = int(input("Please, enter a call cost.\n"))
        break
    except:
        print("Please, enter numbers.")
        continue

# megafon
if userChoiceSelf == 1 and userChoiceInter == 1:
    print(f"Your operator is Megafon and interlocutor's operator is Megafon. Call cost is {userChoiceCost} rubles")
elif userChoiceSelf == 1 and userChoiceInter == 2:
    print(f"Your operator is Megafon and interlocutor's operator is Beeline. Call cost is {userChoiceCost} rubles")
elif userChoiceSelf == 1 and userChoiceInter == 3:
    print(f"Your operator is Megafon and interlocutor's operator is MTS. Call cost is {userChoiceCost} rubles")
elif userChoiceSelf == 1 and userChoiceInter == 4:
    print(f"Your operator is Megafon and interlocutor's operator is Tele2. Call cost is {userChoiceCost} rubles")

# beeline
elif userChoiceSelf == 2 and userChoiceInter == 1:
    print(f"Your operator is Beeline and interlocutor's operator is Megafon. Call cost is {userChoiceCost} rubles")
elif userChoiceSelf == 2 and userChoiceInter == 2:
    print(f"Your operator is Beeline and interlocutor's operator is Beeline. Call cost is {userChoiceCost} rubles")
elif userChoiceSelf == 2 and userChoiceInter == 3:
    print(f"Your operator is Beeline and interlocutor's operator is MTS. Call cost is {userChoiceCost} rubles")
elif userChoiceSelf == 2 and userChoiceInter == 4:
    print(f"Your operator is Beeline and interlocutor's operator is Tele2. Call cost is {userChoiceCost} rubles")

#mts
elif userChoiceSelf == 3 and userChoiceInter == 1:
    print(f"Your operator is MTS and interlocutor's operator is Megafon. Call cost is {userChoiceCost} rubles")
elif userChoiceSelf == 3 and userChoiceInter == 2:
    print(f"Your operator is MTS and interlocutor's operator is Beeline. Call cost is {userChoiceCost} rubles")
elif userChoiceSelf == 3 and userChoiceInter == 3:
    print(f"Your operator is MTS and interlocutor's operator is MTS. Call cost is {userChoiceCost} rubles")
elif userChoiceSelf == 3 and userChoiceInter == 4:
    print(f"Your operator is MTS and interlocutor's operator is Tele2. Call cost is {userChoiceCost} rubles")

#tele2
elif userChoiceSelf == 4 and userChoiceInter == 1:
    print(f"Your operator is Tele2 and interlocutor's operator is Megafon. Call cost is {userChoiceCost} rubles")
elif userChoiceSelf == 4 and userChoiceInter == 2:
    print(f"Your operator is Tele2 and interlocutor's operator is Beeline. Call cost is {userChoiceCost} rubles")
elif userChoiceSelf == 4 and userChoiceInter == 3:
    print(f"Your operator is Tele2 and interlocutor's operator is MTS. Call cost is {userChoiceCost} rubles")
elif userChoiceSelf == 4 and userChoiceInter == 4:
    print(f"Your operator is Tele2 and interlocutor's operator is Tele2. Call cost is {userChoiceCost} rubles")