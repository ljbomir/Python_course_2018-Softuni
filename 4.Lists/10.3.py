vhod = list(map(int, input().split(' ')))
vhod.sort(reverse=True)
lst = []

for x in vhod:
    if x == int(x**0.5) and x >= 0:
        lst.append(x)

print(*lst)
