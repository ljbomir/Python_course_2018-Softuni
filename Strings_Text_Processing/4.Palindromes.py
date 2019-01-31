from operator import itemgetter

data = input().split()

pals = []
for word in data:
    if word[::-1] == word:
        pals.append(word)

pals = sorted(set(pals), key=lambda x: len(x))
print(", ".join(pals))


