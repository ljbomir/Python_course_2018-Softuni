import re
name = input()

pattern = r"\b([A-Z][a-z]+) ([A-Z][a-z]+)\b"

matches=re.findall(pattern, name)
[print(y, end = " ") for x in matches for y in x]

