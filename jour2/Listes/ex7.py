L = [7, 23, 5, 23, 7, 19, 23, 12, 29]

def compterOccurrences(x , list) :
    compter = 0
    for num in list:
        if num == x :
            compter += 1
    
    # return compter
    print(compter)

compterOccurrences(23, L) # 3
compterOccurrences(7, L) # 2
compterOccurrences(100, L)# 0
