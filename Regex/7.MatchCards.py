import re

data = input()
pattern = r'([2-9JQKA]|10)[SHDC]'
output = re.finditer(pattern, data)

[print(x.group(), end = ' ') for x in output]
