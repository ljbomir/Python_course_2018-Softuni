vhod = int(input())


def print_lines(n):
        print( "-"*n*2)


def print_middle(n):
    for i in range(n-2):
        print("-" + "\\/"*(n-1) + "-")

print_lines(vhod)
print_middle(vhod)
print_lines(vhod)
