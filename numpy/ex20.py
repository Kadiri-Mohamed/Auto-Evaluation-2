import numpy as np

age = np.array([20, 30, 40, 50, 60])
salaire = np.array([1500, 2500, 3500, 5000, 8000])
depenses = np.array([800, 1200, 1600, 2000, 3000])

X = np.column_stack((age, salaire, depenses))

print(X[0])

