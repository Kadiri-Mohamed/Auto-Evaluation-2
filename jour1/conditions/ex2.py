# Écrivez un programme Python qui demande le nom d'un employé, son salaire horaire et le nombre
# d'heures travaillées.
# Calculez son salaire total en considérant que les heures travaillées au-delà de 40 heures sont
# rémunérées à 1,5 fois le salaire horaire.
# Affichez le salaire total de l'employé.

name = input("donner votre nom : ")
prenom = input("donner votre prenom : ")
salaire_hor = int(input("donner votre salaire_horaire : "))
nombre_h = int(input("donner votre nombre de heure : "))

salaire_total = 0

if nombre_h > 40 :
    
    salaire_total = salaire_hor * 40
    salaire_total += salaire_hor * (nombre_h - 40 ) * 1.5
     
else :
    salaire_total = salaire_hor * nombre_h
    
    
print("salaire total de" , prenom , name , "est" , salaire_total , "DH")