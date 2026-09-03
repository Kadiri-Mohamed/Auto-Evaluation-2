# Un club privé souhaite contrôler l'accès à ses locaux selon certaines conditions. Une personne est
# autorisée à entrer si :
# • Elle a moins de 18 ans : l'entrée est refusée ;
# • Elle a entre 18 et 25 ans : l'entrée est gratuite ;
# • Elle a plus de 25 ans : l'entrée est autorisée uniquement si elle est membre du club ou
# accompagnée d'un membre.
# Écrivez un programme Python permettant d'afficher le message correspondant à la situation de la
# personne.

age_personne = int(input("Donner votre age : "))

# match age_personne:
#     case 18 > age_personne :

if 18 > age_personne :
    print("l'entree est refusee")
elif (18 < age_personne and 25 > age_personne) or 18 == age_personne :
    print("l'entrée est gratuite")
elif 25 <= age_personne :
    print("l'entrée est autorisée uniquement si elle est membre du club ou accompagnée d'un membre")
        