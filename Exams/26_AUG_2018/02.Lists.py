import re

data = input()

while data != "stop playing":
	new_data = data.replace(" ",'')
	new_data = list(map(int, new_data))
	new_list = []

	if len(set(new_data)) == len(new_data):
		for item in new_data:
			if item % 2 == 0:
				new_list.append(item +2)
			else:
				new_list.append(item)
		new_list = list(map(int, new_list))
		suma = sum(new_list)/len(new_list)
		new_list = sorted(new_list)
		print(f"Unique list: ",end='')
		new_list = list(map(str, new_list))
		print(",".join(new_list))
		print(f"Output: {suma:.2f}")

	else:
		for item in new_data:
			if item % 2 != 0:
				new_list.append(item + 3)
			else:
				new_list.append(item)
		print(f"Non-unique list: ",end='')
		new_list = sorted(new_list)
		suma = sum(new_list)/len(new_list)
		new_list = list(map(str, new_list))
		print(":".join(new_list))
		print(f"Output: {suma:.2f}")

	data = input()



