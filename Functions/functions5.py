x = float(input())
y = float(input())


def triangle(a,b):
    area = (a*b)/2
    return area


area = triangle(x,y)
print(f'{area:.12g}')
