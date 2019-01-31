import re

data = input()
all_names = []

while data != "DEBUG":
	pattern = r"\b32656 19759 32763 0 (?P<size>\d+)\s0\s(?P<name>(\d{2,}|\s)+) 0 \b"
	match = re.finditer(pattern, data)
	for x in match:
		size = x.group('size')
		name = x.group('name')

	name = name.split(' ')
	new_name = ""



	for y in name:
		if y != "":
			new_name += chr(int(y))

	all_names.append(new_name)

	data = input()

for x in all_names:
	print(x)

