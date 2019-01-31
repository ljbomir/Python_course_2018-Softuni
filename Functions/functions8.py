num = abs(int((input())))


def even_odd_multiply(x):
    odd = 0
    even = 0
    rem = 0
    while x != 0:
        rem = x % 10
        if rem % 2 == 0:
            even += rem
        elif rem % 2 == 1:
            odd += rem
        x = int(x/10)
    return odd * even


result = even_odd_multiply(num)
print(result)



