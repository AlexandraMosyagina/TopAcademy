import re

# the first task
# works in format #xxxxxx
hex = re.compile(r'#[0-9A-Fa-f]{6}')
userHex = input("Please, enter a color.\n")
if hex.findall(userHex):
    print(f"{userHex} is a color(s).")
else:
    print(f"{userHex} isn't a color(s).")
# works in format rgb(xxx,xxx,xxx)
rgb = re.compile(r"rgb[(](?:\s*0*(?:\d\d?(?:\.\d+)?(?:\s*%)?|\.\d+\s*%|100(?:\.0*)?\s*%|(?:1\d\d|2[0-4]\d|25[0-5])(?:\.\d+)?)\s*(?:,(?![)])|(?=[)]))){3}[)]")
userRGB = input("Please, enter a color.\n")
if rgb.findall(userRGB):
    print(f"{userRGB} is a color(s).")
else:
    print(f"{userRGB} isn't a color(s).")

# the second task
time = re.compile(r"\d\d:\d\d")
userTime = input("Please, enter your time.\n")
if time.match(userTime):
    print(f"{userTime} is a time.")
else:
    print("Not found.")

# the third task
time = re.compile(r"([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]")
userTime = input("Please, enter your time.\n")
if time.match(userTime):
    print(f"{userTime} is a time.")
else:
    print("Not found.")

# the fourth task
century = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$")
userCentury = input("Please, enter a century.\n")
if century.findall(userCentury):
    print(f"{userCentury} is a century(ies).")
else:
    print(f"{userCentury} isn't a century(ies).")