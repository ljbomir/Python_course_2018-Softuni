input_char = list(input())
chars = {}

for item in input_char:
    if item in chars:
        chars[item] +=1
    else:
        chars[item] = 1

#print(chars)
for item in chars:
    print(f"{item} -> {chars[item]}")
