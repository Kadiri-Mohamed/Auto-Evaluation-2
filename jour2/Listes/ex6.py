L = [10, 20, 30, 40, 50]

def rechercheElement(x ,list ):
    for i in range(len(list)):
        if x == list[i]:
            return i
    
    return False
    

print(rechercheElement(30, L)) # Retourne: 2
print(rechercheElement(100, L)) # Retourne: False