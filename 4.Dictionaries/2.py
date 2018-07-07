input_numbers = list(map(float, input().split(' ')))
numbers = {}

for key in input_numbers:
    if key in numbers:
        numbers[key] += 1
    else:
        numbers[key] = 1


for key in sorted(numbers):
    print(f"{key} -> {numbers[key]} times")

