vhod = list(map(int, input().split(" ")))
vhod.reverse()
lst = []
for i in vhod:
    if i > 0:
        lst.append(i)
        print(i, end = " ")

if len(lst) == 0:
    print("empty")
