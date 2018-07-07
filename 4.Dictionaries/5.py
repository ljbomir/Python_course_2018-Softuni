lst = []
while True:
    data = input()
    if data == "Over":
        break
    else:
        lst.append(data)

dict = {}
for item in lst:
    newdata = item.split(" : ")
    #print(newdata)
    if newdata[0].isdigit():
        dict[newdata[1]] = newdata[0]
    else:
        dict[newdata[0]] = newdata[1]

adict = sorted(dict)
for item in adict:
    print(f"{item} -> {dict[item]}")
