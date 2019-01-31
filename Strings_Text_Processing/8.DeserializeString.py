data = input()
lst = ["" for x in range(200)]

while data != "end":
    data1 = data.split("/")
    char = data1[0].split(":")
    lst[int(char[1])] = char[0]
    for i in data1[1:]:
        lst[int(i)] = char[0]

    data = input()


print("".join(lst))
