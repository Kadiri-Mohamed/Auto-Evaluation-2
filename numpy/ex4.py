import numpy as np

clients = np.array([
    [19,3000,5 ,500],
    [35,8000, 7,3500],
    [28,4500, 5,2100],
    [42,12000, 10,6000],
])


print(f"l age d user est : {clients[0,0]} , revenu : {clients[0,1]}, nombre d'achats : {clients[0,2]}, montant de pense : {clients[0,3]}")

print(f"la colone d age: {clients[0:, 0]}")

print(clients[1:3])

print(f"nombre de dimension est :{ clients.shape}")
print(f"nombre total de clients est :{ clients.shape[0]}")