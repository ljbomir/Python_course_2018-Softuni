nums = input().split(" ")
N = int(input())
numbers = list(map(lambda x: int(x)*N, nums))

#print(*numbers, sep = " ")
print(" ".join(map(str, numbers)))
