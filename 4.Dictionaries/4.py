lst = []

while True:
    data = input()
    if data == "end":
        break
    else:
        lst.append(data)

dict = {}
for item in lst:
    newdata = item.split(" = ")
    if newdata[1] in dict:
        dict[newdata[0]] = int(dict[newdata[1]])
    else:
        dict[newdata[0]] = int(newdata[1])



for key in dict:
    map(int, dict.values())
    print(f"{key} === {dict[key]}")


