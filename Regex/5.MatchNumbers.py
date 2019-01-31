import re

data = input()
pattern = r"(^|(?<=\s))[-]?\d+([.]?\d*)($|(?=\s))"
match = re.finditer(pattern, data)


[print(x.group(), end = " ") for x in match]
