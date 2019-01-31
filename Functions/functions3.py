vhod = int(input())

def print_line(start,end):
    for i in range(1, end+1):
        print(i, end = ' ')
    print()


def triangle(num):
    for i in range(1, num):
        print_line(1,i)
    for k in range(num,0,-1):
        print_line(1,k)


triangle(vhod)

