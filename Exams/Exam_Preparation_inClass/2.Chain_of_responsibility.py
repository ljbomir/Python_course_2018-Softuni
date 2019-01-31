import re

N = int(input())
all_robots = []
manager = None
line = []


for n in range(1,N+1):
	data = input()
	pattern = r"\d+[A-Z][a-z]+([A-Z]|\d){2,}"
	robots = re.finditer(pattern, data)
	robot = re.search(pattern, data)
	pattern2 = r"(!!)$"
	manager = re.search(pattern2, data)
	valid_name = re.search(pattern, data)
	line = [x.group() for x in robots]
	if len(all_robots) >= 2 and len(line) >= 1:
		if all_robots[-1] != line[0]:
			print("Broke the chain!")
			break
	if manager and valid_name:
		print(f"Found the manager!: {valid_name.group()}")
	elif n == N:
		if not manager:
			print(f"Did not find the manager!")

	all_robots.extend(line)

new_robots = []
for x in all_robots:
	if x not in new_robots:
		new_robots.append(x)

print("Chain: " + '->'.join(new_robots))
