nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_carre = [n**2 for n in nombres]
list_pair = [n for n in nombres if n % 2 == 0]
list_nbr_sup_5 = [n for n in nombres if n > 5 ]

print(list_carre)
print(list_pair)
print(list_nbr_sup_5)