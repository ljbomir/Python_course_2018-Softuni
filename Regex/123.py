def callc_number(number):
    if number == 0:
        raise ZeroDivisionError('Cannot be zero')
    else:
        return 5/number

num = int(input())
try:
    result = callc_number(num)
except:
    num = int(num)
