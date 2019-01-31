import re

data = input()

pattern = r"(?P<happy>[;:][\)D*\}\]]|[\(*c\[][:;])|(?P<sad>([\:D\;\(\)]|\])[\(\[\{c\]\;\:])"
m = re.finditer(pattern, data)

sad_count = 0
happy_count = 0
for x in m:
    sad = x.group('sad')
    happy = x.group('happy')
    if sad is not None:
        sad_count += 1
    if happy is not None:
        happy_count += 1

happy_index = float(happy_count) / float(sad_count)
happy_value = None
if happy_index >= 2:
    happy_value = ":D"
elif happy_index > 1:
    happy_value = ":)"
elif happy_index == 1:
    happy_value = ":|"
elif happy_index < 1:
    happy_value = ":("


print(f"Happiness index: {happy_count/sad_count:.2f} {happy_value}")
print(f"[Happy count: {happy_count}, Sad count: {sad_count}]")

