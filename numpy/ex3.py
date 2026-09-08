import numpy as np
etudiants = np.array(["Ali" , "Samir" , "Mehdi" , "Ibrahim"])
matieres = np.array(["Math" , "Physique" , "Arabe"])
notes = np.array([
    [12, 15, 10],
    [8,  14, 18],
    [16, 11, 13],
    [10, 17, 15]
])

moyenne_note = notes.mean(axis=0)
print(moyenne_note)

max_note = notes.max(axis=0)
print(max_note)

min_note = notes.min(axis=0)
print(min_note)

ecarts = max_note - min_note
print(ecarts)
