import numpy as np

employee_salary = np.array([5200 , 1000 , 4000 , 10000])

moyenne = employee_salary.mean() 

print("moyenn:" , moyenne)

medianne = np.median(employee_salary)

print("medianne" , medianne)

variance = employee_salary.var()

print("variance" , variance)

ecart_type = np.std(employee_salary)

print("ecart type :" ,ecart_type)

q1 = np.percentile(employee_salary, 25)
q3 = np.percentile(employee_salary, 75)

print(q1)
print(q3)
