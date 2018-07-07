data = input()
list_separators = [',',':',';','.','!','(', ')','"',"'",'\\','/','[ ]', ' ']

for separator in list_separators:
    data.replace(separator, ' ')

print(data)
list_lower = []
list_upper = []
list_mixed = []

def is_upper(word):
    for letter in word:
        if letter >= 'A' and letter <= 'Z':
            return False
    return True

for word in data.split():
    if word.islower():
        list_lower.append(word)
    elif is_upper(word):
        list_upper.append(word)
    else:
        list_mixed.append(word)

print(f"Lower-case : {', '.join(list_lower)}")
print(f"Mixer-case : {', '.join(list_mixed)}")
print(f"Upper-case : {', '.join(list_upper)}")

