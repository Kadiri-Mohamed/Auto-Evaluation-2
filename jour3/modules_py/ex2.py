from datetime import datetime , date
# import math

liste1 = ["15/08/2025", "20/08/2023", "08/02/2017", "23/04/2009"] # Jour / Mois / Année
liste2 = ["2025-03-18", "2022-04-23", "2019-06-12", "2008-01-10"] # Année - Mois - Jour

list3 = [(datetime.strptime(n , "%d/%m/%Y")).strftime("%Y-%m-%d") for n in liste1]


for i , j in zip(liste2,list3):
    print(f"defference between {i} et {j} est : {abs((datetime.strptime(i , "%Y-%m-%d") - datetime.strptime(j , "%Y-%m-%d")).days)} days")
# print(list3)