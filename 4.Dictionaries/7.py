data = input()
user_logins = {}

while data != "login":
    lst = data.split()
    user = lst[0]
    passwd = lst[2]
    user_logins[user] = passwd
    data = input()


#print(user_logins)

data = input()
counter = 0
while data != "end":
    key = data.split()[0]
    value = data.split()[2]
    for user,passwd in user_logins.items():
        if key == user:
            if value == passwd:
                print(f"{key}: logged in successfully")
            else:
                print(f"{key}: login failed")
                counter += 1
        elif key not in user_logins.keys():
            print(f"{key}: login failed")
            counter += 1
            break
    data = input()

print(f"unsuccessful login attempts: {counter}")