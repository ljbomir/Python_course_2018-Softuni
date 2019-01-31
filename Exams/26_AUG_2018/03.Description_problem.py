import re

data = input()


class Person:
	def __init__(self, _name, _age, _born):
		self.name = _name
		self.age = _age
		self.born = _born


persons = []

while data != "make migrations":
	name_age_born = r"my name is (?P<name>[A-Z]\w+\s[A-Z]\w+).(.*)\s(?P<age>\d{2}) years(.*) on (?P<born>\d{2}-\d{2}-\d{4}).$"
	nab_match = re.finditer(name_age_born, data)
	valid = re.search(name_age_born, data)
	if valid:
		name_ = None
		age_ = None
		born_= None
		for x in nab_match:
			name_ = x.group('name')
			age_ = x.group('age')
			born_ = x.group('born')

		per = Person(_name=name_,_age=age_,_born=born_)
		persons.append(per)
		
	data = input()
if len(persons) > 0:
	for person in persons:
		print(f"Name of the person: {person.name}.")
		print(f"Age of the person: {person.age}.")
		print(f"Birthdate of the person: {person.born}.")
else:
	print("DB is empty")

