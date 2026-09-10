import numpy as np

arr = np.array([
    [2,3],
    [1,3],
    [7,8]
])

c1 = arr[0]

rest = arr[1:]

dist_eq = np.sqrt(( rest[0] - c1[0] )**2 + ( rest[1] - c1[1] )**2 )

print(dist_eq)