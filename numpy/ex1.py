import numpy as np


arr = np.array([1200.50, 1550.00, 980.75, 2100.00, 1750.25])

print(f"type de tablau: {type(arr)}" )
print(f"shape de tablau: {arr.shape}" )
print(f"nombre dimension de tablau: {arr.ndim}" )
print(f"size de tablau: {arr.size}" )
print(f"data type de tablau: {arr.dtype}" )
print(f"1ere valeur de tablau: {arr[0]}" )
print(f"last valeur de tablau: {arr[-1]}" )
print(f"max valeur de tablau: {arr.max()}" )
print(f"moyenne valeur de tablau: {arr.mean()}" )
print(f"min valeur de tablau: {arr.min()}" )