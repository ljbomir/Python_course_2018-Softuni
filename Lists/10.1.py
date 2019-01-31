import random

#vhod = list(map(int, input().split(" ")))
#lst = []


def program(y):
    #y.split(" ")
    y.sort(reverse=True)
    print(y)
    lst = []
    for x in y:
        if (x**0.5)**2 == int(x) and x > 0:
            lst.append(x)
    print(*lst)


def test_case():
    lst = []
    for x in range(30):
        lst.append(random.randint(-20,103))
    print(*lst)


y = test_case()
#print(y)
#print(type(y))
#program(y)

