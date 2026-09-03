list_p = [1, 2, 3, 4, 5]  

list_carre = [n**2 for n in list_p ]

list_carre.append(36)

assert len(list_carre) == len(list_p) , "Attention les 2 listes n'ont pas la même taille"

print(list_carre)