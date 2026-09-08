import numpy as np


arr = np.array([
    [20 , 3000 , 3 , 200],
    [40 , 8000 , 7 , 380],
    [35 , 12000 , 5 , 190],
])


clients_et = arr[(arr[:,0] > 30) & (arr[:,1] > 10000)]
clients_or = arr[~(arr[:,0] < 30) | (arr[:,1] > 10000)]

nb_clients = len(clients_or)


print("condition with and :" ,clients_et)
print("condition with or :",clients_or)
print("nb :",nb_clients)