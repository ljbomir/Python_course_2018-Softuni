import re

data = input()
pattern = r"\b(0x)?[0-9A-F]+\b"
match = re.finditer(pattern, data)

[print(x.group(), end=" ") for x in match]
