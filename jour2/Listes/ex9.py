text1 = "hello labas !"
text2 = "Ach khbark hanya ?"

text3 = text1.split() + text2.split()

resultat = []

for i in text3:
    i = i.lower()

    if len(i) <= 3:
        resultat.append(i)

print(resultat)

for i in text3 :
    for j in resultat:
        if i.lower() == j :
            print(j)