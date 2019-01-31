vhod = list(map(int, input().split(" ")))


for x in range(len(vhod)):
 if vhod[x] % 2 != 0 and x % 2 != 0:
     print(f"Index {x} --> {vhod[x]}")


###########################################

#vhod = list(map(int, input().split(" ")))

#counter = 0
#for x in vhod:
#    if x % 2 != 0:
#        if not counter % 2 == 0:
#            print(f"Index {counter} -> {x}")
#    counter += 1
