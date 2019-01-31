inventory = input().split(' ')

data = input()

while data != "Fight!":
	data = data.split(' ')
	command = data[0]
	equipment = data[1]
	if command == "Buy":
		inventory.append(equipment)
	if command == "Trash":
		if equipment in inventory:
			inventory.remove(equipment)
	if command == "Repair":
		if equipment in inventory:
			inventory.append(inventory.pop(inventory.index(equipment)))
	if command == "Upgrade":
		if equipment.split('-')[0] in inventory:
			equ_index = inventory.index(equipment.split('-')[0])
			new_equipment = equipment.split('-')[0] + ":" + equipment.split('-')[1]
			if len(inventory) > equ_index:
				inventory.insert((equ_index+1),new_equipment)

	data = input()

print(*inventory)

