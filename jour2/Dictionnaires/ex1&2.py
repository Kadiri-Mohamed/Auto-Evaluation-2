etudiant = {
 "nom": "Omar", "age": 22,
 "ville": "Casablanca", "note": 15
}

print(f"nom: {etudiant['nom']}, âge: {etudiant['age']} et note: {etudiant['note']}")

etudiant["note"] = 17

print(f"nom: {etudiant['nom']}, âge: {etudiant['age']} et note: {etudiant['note']}")

etudiant["formation"] = "IA"

print(f"nom: {etudiant['nom']}, âge: {etudiant['age']} et note: {etudiant['note']} et formation: {etudiant['formation']}")




produit = {
 "nom": "Ordinateur", "prix": 8500,
 "stock": 12, "categorie": "Informatique"
}

produit["prix"] = 7900
produit["marque"] = "Lenovo"
produit["disponible"] = True

print(f"marque: {produit['marque']}, prix: {produit['prix']} et stock: {produit['stock']} et categorie: {produit['categorie']}")

del produit["stock"]
print(f"marque: {produit['marque']}, prix: {produit['prix']} et categorie: {produit['categorie']}")


