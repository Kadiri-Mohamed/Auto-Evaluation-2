notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

# print(notes)

# somme = 0
 
# for i in notes:
#     somme += i
    
# print (f"moyenne est :  , {somme / len(notes):.2f}")


notes_sup_10 = []
notes_inf_10 = []

for i in notes:
   if i >= 10 :
       notes_sup_10.append(i)
   else:
       notes_inf_10.append(i)

# print(notes_sup_10)
# print(notes_inf_10)


# meilleure_note = max(notes)
# mauvaise_note = min(notes)

# print(mauvaise_note)
# print(meilleure_note)

print(f"{(len(notes_sup_10) / len(notes) * 100):.2f} %")