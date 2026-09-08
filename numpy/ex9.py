import numpy as np

"""
    [
        mois1   moi2  mois3
        [12      34     23] Produit A
        [32      89     20] Produit B
        
        
        each value = qte
    ]
"""

ventes = np.array([
    [100, 120, 150],
    [130, 140, 160], 
    [80,  90,  110]
])

vente_total_p = ventes.sum(axis=1)
vente_moyenne_p = ventes.mean(axis=1)

vente_total_m = ventes.sum(axis=0)
vente_moyenne_m = ventes.mean(axis=0)

meilleur_produit = np.argmax(np.sum(ventes , axis=1))
meilleur_mois = np.argmax(np.sum(ventes , axis=0))

print(vente_total_p)
print(vente_total_m)

print(vente_moyenne_p)
print(vente_moyenne_m)

print(meilleur_produit)
print(meilleur_mois)