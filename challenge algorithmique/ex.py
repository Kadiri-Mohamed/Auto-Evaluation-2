import math
def factorielle(x:int) -> int:
    fac = 1
    for i in range(1,x+1):
        fac *= i
    return fac

# print(factorielle(0))


def multiplication_10 (n:int) :
    for i in range(0,11):
        print(f"{n} x {i} = {n*i}")
        
# multiplication_10(3)

def carre_parfait(l:int):
    racine = math.isqrt(l)  
    res = racine * racine == l
    
    if res:
        print("carre parfait")
    else:
        print("carre non parfait")
        
        
carre_parfait(5)

# print(math.sqrt(5))  


def chaine_carac_un_un(text:str):
    for i in text:
        print(i)
        
# chaine_carac_un_un("hello world")


def mot_plus_long(phrase):
    list_mots = phrase.split()
    long_mot = list_mots[0]
    
    for i in list_mots:
        if len(long_mot) < len(i):
            long_mot = i
            
    return long_mot

# print(mot_plus_long("Hello I'm Mohamedddd from Errachidia"))


def occ_char_in_phrase(text):
    dics = {}
    
    for i in text:
        if i not in dics:
            dics[i] = 1
        else :
            dics[i] += 1
            
    return dics

# print(occ_char_in_phrase("hello world"))