import numpy as np

age = np.array([20, 30, 40, 50, 60])
salaire = np.array([1500, 2500, 3500, 5000, 8000])
depenses = np.array([800, 1200, 1600, 2000, 3000])

arr = np.column_stack((age, salaire, depenses))

# print(arr[:,0])

min_arr = np.min(arr , axis=0)
max_arr = np.max(arr , axis=0)

# print(min_arr)
# print(max_arr)

moyenne = np.mean(arr)
ecart_type = np.std(arr)

arr_normalised = (arr - min_arr) / (max_arr - min_arr)

# print(arr_normalised)

arr_standardised = (arr - moyenne) / ecart_type 

print(arr_standardised)
print(np.mean(arr_standardised))
print(np.std(arr_standardised))


