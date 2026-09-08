import numpy as np

temperatures = np.array([
    [1 , 2, 3 , 4] ,
    [32 , 37 , 35 , 39]
])

t = temperatures[1]
moyenne = t.mean()

# print(moyenne)

max_temp = np.max(t)
min_temp = np.min(t)

temp_sup_moyenne = t[t>moyenne]

amplitude_th = max_temp - min_temp

#diff
variations = np.diff(t)


print("Moyenne :", moyenne)
print("Maximum :", max_temp)
print("Minimum :", min_temp)
print("Temp sup 10 :", temp_sup_moyenne)
print("Ampplitude Thermique :", amplitude_th)
print("variations entre jours consecutifs:", variations)