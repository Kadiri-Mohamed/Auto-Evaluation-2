import numpy as np

clients = np.array([
    ["mohamed amine",19,3000,5 ,500],
    ["mohamed kadiri",35,8000, 7,3500],
    ["mohamed mehdi",28,4500, 5,2100],
    ["mohamed ali",42,12000, 10,6000],
])


clients[0 , 1] = 21 
clients[0 ] = ["Aymane kabiri",18,567, 2,1234] 

print(clients[3])
print(clients[3 , 4])
print(clients[3 , 0:3])

print(clients)


clients_copy = clients.copy()

# print(clients_copy)

# np.delete(clients_copy , [3 , 4])

clients_copy[3,4] = 4444

print(clients_copy)
