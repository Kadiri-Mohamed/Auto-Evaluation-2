# La suite de Syracuse (aussi appelée suite de Collatz ou conjecture de Syracuse) est une suite définie pour un entier naturel positif n comme suit :

# Si n est pair, le terme suivant est n // 2.

# Si n est impair, le terme suivant est 3n + 1.

# La suite se termine lorsque n devient égal à 1.

# Écrire un code permettant de calculer cette suite

number = int(input("Donner un nombre pour tester La suite de Syracuse : "))
list = []
while number != 1 :
    if number % 2 != 0 :
        number = (3 * number) + 1
    else :
        number = number // 2 
    list.append(number)
        
print(list)