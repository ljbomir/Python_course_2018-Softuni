vhod = input().split("|")
lst = []

counter = 0
for i in vhod[::-1]:
    lst += i.split()

print(*lst)
