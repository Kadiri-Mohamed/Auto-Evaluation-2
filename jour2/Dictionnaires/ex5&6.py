noms = ["Python", "SQL", "Pandas", "NumPy"]
niveaux = [5, 4, 3, 4]

t = zip(noms , niveaux)
res = {}
for c , v in zip(noms , niveaux):
    res[c] = v
    
# print(res)

etudiant = {
 "nom": "Omar", "age": 22,
 "formation": {"nom": "Développement IA", "niveau": "Avancé", "duree": 12}
}

etudiant["formation"]["niveau"] = "Expert"
etudiant["technologies"] = ["Python", "SQL", "Pandas", "Machine Learning"]

print(etudiant)
