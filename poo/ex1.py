import dataclasses 

# @dataclasses
class Vehicule:
    def __init__(self,marque,vitesse_max):
        self._marque = marque
        self.__vitesse_max = vitesse_max
        
    # def __str__(self):
    #     return f"La marque de Vehicule est :{self._marque} , sa vitesse max est : {self.__vitesse_max}"
    
    def __eq__(self, value):
        return self.__vitesse_max == value.__vitesse_max
    
    def deplacer(self):
        return "Move :"



class Voiture(Vehicule):
    def __init__(self, marque, vitesse_max, portes):
        super().__init__(marque, vitesse_max)
        self.portes = portes
        
    def __str__(self):
            return f"La marque de voiture est :{self._marque} , sa vitesse max est : {self._Vehicule__vitesse_max}"
        
    def deplacer(self):
        return "move sur 4 O"
        

class Moto(Vehicule):
    # def __init__(self, marque, vitesse_max):
    #     super().__init__(marque, vitesse_max)
    
    def __str__(self):
            return f"La marque de Moto est :{self._marque} , sa vitesse max est : {self._Vehicule__vitesse_max}"
        
    def deplacer(self):
            return "move sur 2 O"
        

v1 = Voiture("Mercides" , 220 , 4)
v2 = Voiture("Audi" , 130 , 4)
v3 = Voiture("BMW" , 290 , 4)
m1 = Moto("BMW" , 190)
m2 = Moto("Yamaha" , 300)

listes_des_viecules = [v1 , v2 , v3 , m1 , m2]

# print(v1)
print(m2)
for i in listes_des_viecules:
    # print(i)
    print(i.deplacer())
    
# print(v1 == v1)

    