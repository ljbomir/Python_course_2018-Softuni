data = input()
all_chars = {}
lst = ["" for x in range(200)]

while data != "end":
    data = data.split("/")
    char = data[0].split(":")[0]
    first_index = data[0].split(':')[1]
    all_chars[char] = [first_index]
    for i in data[1:]:
            all_chars[char].append(i)

    data = input()


for k,v in all_chars.items():
    for i in v:
        lst[int(i)] = k

print("".join(lst))
