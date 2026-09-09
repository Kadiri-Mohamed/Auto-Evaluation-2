import numpy as np
import math 

numbers = np.array([11,np.nan,23,10,np.nan,np.nan])

# print(numbers[~np.isnan(numbers)])

print(np.where(np.isnan(numbers)))

moyenne = np.nanmean(numbers)

numbers[np.isnan(numbers)] = moyenne

print(moyenne)
print(numbers)

