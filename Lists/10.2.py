import math
numbers = list(map(int, input().split(' ')))
numbers.sort(reverse=True)
for item in numbers:
    if item >= 0:
        result = math.sqrt(item)
        if result == int(result):
            print(int(item), end=' ')
