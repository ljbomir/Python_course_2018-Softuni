import re

data = input()
pattern = r"<\w+>"
match = re.findall(pattern, data)
match1 = re.search(pattern, data)

caratValueOfTheDiamond = 0

if not match1:
    print(f"Better luck next time")
else:
    for x in match:
        for y in x:
            if y.isdigit():
                caratValueOfTheDiamond += int(y)
        print(f"Found {caratValueOfTheDiamond} carat diamond")
        caratValueOfTheDiamond = 0


