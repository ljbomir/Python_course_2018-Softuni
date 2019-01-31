data = input()


class Gladiator:
	def __init__(self, name, skill, total=0):
		self.skill = skill
		self.name = name
		self.total = total


all_skills = {}
all_names = []
while data != "Ave Cesar":
	if len(data.split('->')) == 3:
		name, technique, skills = data.split(" -> ")
		all_skills[technique] = int(skills)
		for x in all_names:
			if name == x.name:
				x.skill[technique] = int(skills)
				x.total += x.skill[technique]
		if not any(x.name == name for x in all_names):
			name = Gladiator(name, all_skills)
			all_names.append(name)
			name.total += name.skill[technique]
			all_skills = {}


	elif len(data.split('vs')) == 2:
		name1, name2 = data.split("vs")

	data = input()

for x in all_names:
	print(f"{x.name}: {x.total} skill")
	for y,j in x.skill.items():
		print(f" - {y} <!> {j}")



