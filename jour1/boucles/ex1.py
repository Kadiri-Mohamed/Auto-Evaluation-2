# Écrivez un programme Python qui demande à l'utilisateur de saisir un nombre entier N, puis calcule et
# affiche la somme de tous les entiers compris entre 1 et N


x = int(input("Donner un nombre : "))
somme = 0
for i in range(1 , x+1):
    somme += i
    
print(somme)