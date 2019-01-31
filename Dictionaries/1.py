input = input().split(' ')
dicts = {}

for key in input:
    if key.lower() in dicts:
        dicts[key.lower()] += 1
    else:
        dicts[key.lower()] = 1

lst = []
for key in dicts:
    if dicts[key] % 2 != 0:
        lst.append(key)


print(", ".join(lst))
