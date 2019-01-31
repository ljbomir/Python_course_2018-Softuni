import re

first_line = input()
character = first_line[0]
count = int(first_line[1])
data = input()

char_list = []
counter = 0

while data != 'end':
    pattern = r'^[A-Z].*[!.?]$'
    match = re.findall(pattern, data)
    words = re.findall(r'\w+', str(match))
    for word in words:
        for char in word:
            if char == character:
                counter += 1
        if counter >= count:
                char_list.append(word)

        counter = 0

    data = input()

print(", ".join(char_list))
