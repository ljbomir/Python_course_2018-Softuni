import re

data = input().strip('[]')

first_char = int(data.split(',')[0].replace("\"",''))
last_char = int(data.split(',')[1].replace("\"",''))
word = data.split(',')[2].replace("\"",'').strip(' ')

country = r"\b[A-Z]\w+[A-Z]\b"
code = r"\d{3}"
rounded = r"\d{3}\.\d+"

country_match = (re.search(country, data)).group().capitalize()
to_be_rounded = re.findall(rounded, data)
code_match = re.findall(code, data)

city = ''
if len(to_be_rounded) > 0:
	#roundung up a digits and add them in a list
	digits = []
	for digit in to_be_rounded:
		digit = int(float(digit))
		if digit == round(digit/1):
			digit = int(digit) + 1
		else:
			digit = int(digit)
	digits.append(digit)

	#replacing not rounded digits with rounded
	new_code_match = ''
	for digit in digits:
		for x in to_be_rounded:
			new_code_match = data.replace(x,str(digit))
	codes = re.findall(code, new_code_match)
	for code in codes:
		code = chr(int(code))
		city += code
else:
	for char in code_match:
		char = chr(int(char))
		city += char

City = city.capitalize()
a = country_match[first_char:last_char+1]
Country = country_match.replace(a, word)

print(Country," => ", City)




