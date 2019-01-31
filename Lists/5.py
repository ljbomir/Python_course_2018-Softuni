nums = list(map(int, input().split(" ")))
suma = 0

for x in nums:
    if x % 2 != 0:
        suma += 1

print(suma)
