# Écrivez un programme Python qui demande à l'utilisateur de saisir une chaîne de caractères, puis
# affiche cette chaîne inversée.

# text = input("donner une chaine de caractere : ")
text = "Salam"
list = ""
for i in range(len(text)-1,-1,-1):
    # print(text[i])
    list += text[i]

newtext = ""
for i in list:
    newtext += i
print(newtext)




# print(text[::-1])
# print(text[::-1])
# print(text[:0:-1])
# print(text[0:len(text)+1:-1])
     