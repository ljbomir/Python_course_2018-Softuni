z = input()
x = input()
y = input()


def char(a, b):
    if ord(a) > ord(b):
        return a
    else:
        return b


def integer(a, b):
    if a > b:
        return a
    else:
        return b


def string(a, b):
    if a > b:
        return a
    else:
        return b


def type_of_input(z):
    if z == "char":
        return char(x,y)
    elif z == "int":
        return integer(x,y)
    elif z == "string":
        return string(x,y)


print(type_of_input(z))
