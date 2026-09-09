import numpy as np

arr = np.array([3,4,5,100])

q1 = np.percentile(arr , 25)
q3 = np.percentile(arr , 75)

# print(q1 , q3)

# IQR=Q3−Q1

iqr = q3 - q1

# print(iqr)

# Limitebasse=Q1-1.5xIQR
# Limitehaute=Q3+1.5×IQR

limite_basse = q1-1.5 * iqr
limite_haute = q1+1.5 * iqr

# print(limite_basse)
# print(limite_haute)

annomalies = (arr < limite_basse) | (arr > limite_haute)

print(annomalies)

























# moyenne = np.mean(arr)
# ecart_type = np.std(arr)

# anormales = arr[
#     (arr > moyenne + 2 * ecart_type) |
#     (arr < moyenne - 2 * ecart_type)
# ]
# print(moyenne + 2 * ecart_type)

# print(ecart_type)
# print(anormales)