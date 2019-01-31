data = (input()).lower()
sub = input()


def occurrences(text, sub):
    c = n = 0
    #text.find(sub)
    while n != -1:
        c += 1
        n = text.find(sub, n+1)
    return c


print(occurrences(data,sub))
