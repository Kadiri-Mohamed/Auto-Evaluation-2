import pandas as pd
import numpy as np
data = pd.read_csv("ventes.csv")

# print(data)

chiffre_affaires = data["prix"] * data["quantite"]
chiffre_affaire_total = ( data["prix"] * data["quantite"])*2

tva = chiffre_affaires * 20 / 100
prix_avec_tva = chiffre_affaires - tva

# print(chiffre_affaires)

# print("chiffre affaire total: \n",chiffre_affaire_total)
# print("tva des chiffre affaire: \n",prix_avec_tva)


t = pd.cut(chiffre_affaires , 
           bins=[0,1000 , 5000 , float("inf")],
           labels=["Fiable" , "Moyen" , "Eleve"],
           )

# print(t)

# data["categorie_prix"] = t

# print(data)

data["categorie_qte"] = np.where(
    data["quantite"] >= 10 ,
    "huge" ,
    "small"
)
print(data)