data = input()
all_chars = {}

for i,x in enumerate(data):
    if x in all_chars:
        all_chars[x].append(i)
    else:
        all_chars[x] = [i]

for value,key in all_chars.items():
    lst = "/".join(list(map(str, key)))
    print(f"{value}:{lst}")
