import numpy as np

prix = np.array([120, 340, 800])
remise = np.array([10, 6, 7])
qte = np.array([12, 10, 8])

montant = prix * qte

montant_remise = montant * remise / 100

vente = montant - montant_remise

tva = vente * 20 / 100

vente_ttc = vente + tva

ca = np.sum(vente_ttc)

nombre_ventes = len(vente_ttc)

vente_moyenne = np.mean(vente_ttc)

vente_min = np.min(vente_ttc)

vente_max = np.max(vente_ttc)

print("CA avec TVA :", ca, "DH")
print("Nombre de ventes :", nombre_ventes)
print("Vente moyenne :", vente_moyenne, "DH")
print("Vente minimale :", vente_min, "DH")
print("Vente maximale :", vente_max, "DH")