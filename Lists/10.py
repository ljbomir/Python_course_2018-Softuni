import math

vhod = list(map(int, input().split(" ")))
lst = []
 
for x in vhod:
   if x > 0 and math.sqrt(x) == int(math.sqrt(x)):
       lst.append(x)

lst.sort(reverse = True)
print(*lst)
