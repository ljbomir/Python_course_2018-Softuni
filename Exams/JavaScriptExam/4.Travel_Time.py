data = input().strip('[] ')
data = data.split(',')

travel = {}


for item in data:
	country, town, cost = item.strip('"').split(' > ')
	town = town.capitalize()
	cost = int(cost)
	if country not in travel:
		temp_dict = {town: cost}
		travel[country] = temp_dict
	else:
		if town in travel[country]:
			if cost < travel[country][town]:
				travel[country][town] = cost
		elif town not in travel[country]:
			travel[country][town] = cost

sorted_travel = sorted(travel, key=lambda x: x[0])


for country in sorted_travel:
	sorted_towns = sorted(travel[country].items(), key=lambda x: x[1])
	print(country,"->",end=' ')
	for pair in sorted_towns:
		print(pair[0],"->",pair[1], end='')

	print()

