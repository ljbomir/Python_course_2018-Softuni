string = input()
data = input()

while data != "end":
    data = data.split()
    command = data[0]
    count = int(data[1])
    i = 1
    while i <= count:
        if command == 'Right':
            string = string[-1] + string[0:-1]
            i += 1
        elif command == "Left":
            string = string[1:] + string[0]
            i += 1
        else:
            break

    if command == "Insert":
        a = string[:count]
        b = string[count:]
        string = a + data[2] + b
    elif command == "Delete":
        a = string[:count]
        b = string[int(data[2])+1:]
        string = a + b

    data = input()

print(string)