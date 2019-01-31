import re
data = input()

pattern = r"\b(?P<day>\d{2})([\.\-\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
match = re.finditer(pattern, data)


for match in match:
    year = match.group('year')
    month = match.group('month')
    day = match.group('day')
    print(f"Day: {day}, Month: {month}, Year: {year}")
