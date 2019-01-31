import re

phone = input()
pattern = r"\+\b359([ -])2\1\d{3}\1\d{4}\b"

matches = re.finditer(pattern, phone)
[print(x.group(), end=" ") for x in matches]

