numbers = input().split(" ")
lst = []
P = int(input())

count = 0
for i in numbers:
    lst.append(int(i)*P)
    print(lst[count], end = " ")
    count += 1
