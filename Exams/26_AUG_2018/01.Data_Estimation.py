from datetime import *

today = date.today()
data = input().split('-')
year = int(data[0])
month = int(data[1])
day = int(data[2])

future = date(year,month,day)
diff = (future - today).days


if diff <= 0:
	print("Passed")

elif diff == 0:
	print("Today date")

elif diff > 0:
	if diff == 1:
		print(f"{diff+1} dayl left")
	else:
		print(f"{diff+2} days left")

