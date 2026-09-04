import math

def charger_villes(chemin):
    with open(chemin,'r') as file:
        content = file.readlines()
    
    villes = []

    for i in content:
        cord = i.split()
        villes.append((" ".join(cord[:-2]), float(cord[-2]), float(cord[-1])))
        
    return villes

# print(charger_villes("villes.txt"))
        
        
def distance_euclidienne(villeA, villeB):
    d = math.sqrt(math.pow((villeB[1] - villeA[1]),2)+math.pow((villeB[2] - villeA[2]),2))
    # print(f"La distance euclidienne entre {villeA[0]} et {villeB[0]} est: {d:.2f}°")
    return d

# distance_euclidienne(('Paris', 48.8567, 2.3522),('Bordeaux', 44.84, -0.58))


def itineraire_greedy(villes):
    ville_act = villes[0]
    list_villes_ord = [ville_act]
    villes_restantes = villes[1:]

    while villes_restantes:
        ville_next = villes_restantes[0]
        distance_min = distance_euclidienne(ville_act, ville_next)

        for ville in villes_restantes:
            distance = distance_euclidienne(ville_act, ville)

            if distance < distance_min:
                distance_min = distance
                ville_next = ville

        list_villes_ord.append(ville_next)
        villes_restantes.remove(ville_next)
        ville_act = ville_next

    return list_villes_ord

print(itineraire_greedy(charger_villes("villes.txt")))


def distance_totale(itineraire):
    somme = 0
    for i in range(0,len(itineraire)-1):
        somme += distance_euclidienne(itineraire[i],itineraire[i+1])
        
    return somme

# print(f"distance total est: {distance_totale(itineraire_greedy(charger_villes("villes.txt"))):.2f}")


def recapitulatif():
    # print("----------- les villes: -----------\n")
    # for i in charger_villes('villes.txt'):
    #     print(i)
    villes = charger_villes('villes.txt')
    print(f"nombre de villes trouvee est: {len(villes)}")
    
    itineraire_trouve = itineraire_greedy(villes)
    
    print(itineraire_trouve)
    
    distance_totale1 = distance_totale(itineraire_trouve)
    print(f"la distance total est: {distance_totale1:.2f}")
        
    
        
    
                  
     
# recapitulatif()
    