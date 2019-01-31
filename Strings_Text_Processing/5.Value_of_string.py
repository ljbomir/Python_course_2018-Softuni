data = input()
low_or_up = input()

lst_low = []
lst_up = []
lst_chars = []

for char in data:
    if char.isalpha():
        if char.isupper():
            lst_up.append(ord(char))
        elif char.islower():
            lst_low.append(ord(char))

if low_or_up == "UPPERCASE":
    print(f"The total sum is: {sum(lst_up)}")
elif low_or_up == "LOWERCASE":
    print(f"The total sum is: {sum(lst_low)}")
