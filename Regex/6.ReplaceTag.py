import re
data = input()

while data != "end":
    pattern = r'<a\s?href=(.*)>(.*)<\/a>'
    repl = r'[URL href=\1]\2[/URL]'
    replaced = re.sub(pattern, repl, data)
    print(replaced)

    data = input()




