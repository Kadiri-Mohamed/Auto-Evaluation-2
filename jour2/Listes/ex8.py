L = [7, 23, 5, 23, 7, 19, 23, 12, 29, 7, 5]

list = {}
for x in L:
    if x not in list:
        list[x] =  1
    else :
        list[x] = list[x] + 1
        
print(list)
        