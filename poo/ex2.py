
from dataclasses import dataclass

@dataclass
class Voiture:
    marque : str = "Tesla"
    model : str = "Model 3"
    prix : float | int = 35000
    kilometrage : int = 10000
    
    def afficher_info(self):
        print(f"""
Marque: {self.marque}
Model: {self.model}
Prix: {self.prix}
kilometrage: {self.kilometrage}""")
    
    
    
v1 = Voiture("Range river", "Q5" , 200000 , 3000)
# v2 = Voiture()
# print(v1)

# v2.afficher_info()

@dataclass
class VoitureElectrique(Voiture):
    autonomie : int | float = 0
    
    def afficher_info(self):
            print(f"""
Marque: {self.marque}
Model: {self.model}
Prix: {self.prix}
kilometrage: {self.kilometrage}
Autonomie: {self.autonomie} km""")
    

ve1 = VoitureElectrique("Audi", "Q5" , 200000 , 3000 , 2000)
ve1.afficher_info()

@dataclass
class Concession:
    nom: str
    inventaire: list = field(default_factory=list)

    def ajouter_voiture(self, voiture: Voiture | VoitureElectrique):
        self.inventaire.append(voiture)

    def afficher_inventaire(self):
        for voiture in self.inventaire:
            voiture.afficher_info()

    def vendre_voiture(self, marque, model):
        for voiture in self.inventaire:
            if voiture.marque == marque and voiture.model == model:
                print(f"La voiture {voiture.marque} {voiture.model} a ete vendue")
                return

        print("La voiture n'a pas ete trouvee")