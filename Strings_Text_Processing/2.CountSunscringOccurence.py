data = (input()).lower()
sub = (input()).lower()

count = 0
for i in range(len(data)):
    if data[i:].startswith(sub):
        count += 1

print(count)

