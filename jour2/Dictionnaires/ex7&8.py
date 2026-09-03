# 7 -

etudiants = [
    {"nom": "Omar", "age": 22, "note": 15},
    {"nom": "Sara", "age": 21, "note": 17},
    {"nom": "Yassine", "age": 23, "note": 9},
    {"nom": "Imane", "age": 20, "note": 13},
    {"nom": "Hamza", "age": 24, "note": 7}
]

# for etudiant in etudiants:
#     if etudiant["note"] >= 10:
#         print(etudiant["nom"], ": Admis")
#     else:
#         print(etudiant["nom"], ": Echec")

total = 0

for etudiant in etudiants:
    total += etudiant["note"]

moyenne = total / len(etudiants)

# print("Moyenne de la classe :", moyenne)

meilleur = etudiants[0]

for etudiant in etudiants:
    if etudiant["note"] > meilleur["note"]:
        meilleur = etudiant

# print("Meilleure :", meilleur["nom"])

# 8 -

ventes = [
 {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 2},
 {"produit": "Souris", "categorie": "Accessoire", "prix": 150, "quantite": 10},
 {"produit": "Clavier", "categorie": "Accessoire", "prix": 300, "quantite": 5},
 {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 1},
 {"produit": "Écran", "categorie": "Informatique", "prix": 2500, "quantite": 3}
]

# nb_total_ven = 0
chiffre_aff = 0
qte_t_v = 0
p_plus_chere = ventes[0]

for vente in ventes:
    # nb_total_ven += 1
    chiffre_aff += vente["prix"] * vente["quantite"]
    qte_t_v += vente['quantite']
    if p_plus_chere['prix'] < vente["prix"]:
        p_plus_chere = vente
    
    
    
# print("nb vente:" ,len(ventes))
# print("chiffre affaire:",chiffre_aff)
# print("produit plus chere:",p_plus_chere)
# print("qte total des ventes:",qte_t_v)


ca_produits = {}
for vente in ventes:
    produit = vente["produit"]
    ca = vente["prix"] * vente["quantite"]

    if produit in ca_produits:
        ca_produits[produit] += ca
    else:
        ca_produits[produit] = ca
        
        
print(ca_produits)

produits_categories = {}

for vente in ventes:
    categorie = vente["categorie"]

    if categorie in produits_categories:
        produits_categories[categorie] += 1
    else:
        produits_categories[categorie] = 1
    

print(produits_categories)