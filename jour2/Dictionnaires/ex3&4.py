notes = {"Python": 15, "SQL": 13, "JavaScript": 17, "Git": 14, "Linux": 12}

# print(notes.keys())
# print(notes.values())
# print(notes.items())

max_num = max(notes.values())
min_num = min(notes.values())
moyenne = sum(notes.values()) / len(notes)

# print(max_num)
# print(min_num)
# print(moyenne)

notes_etudiants = {"Omar": 15, "Sara": 8, "Yassine": 17, "Imane": 11, "Hamza": 6, "Nadia":14}

etudiants_sup_10 = {}
etudiants_min_10 = {}

for c ,v in notes_etudiants.items():
    if v >= 10 :
        etudiants_sup_10[c] = v
    else :
        etudiants_min_10[c] = v
        
print(etudiants_min_10)
print(etudiants_sup_10)

print(max(etudiants_sup_10.values()))

print((len(etudiants_sup_10) / len(notes_etudiants)) * 100)
