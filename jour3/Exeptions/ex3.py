class ParametreError(Exception):
    pass

def calculer_carre(x):
    """Fonction calcule le carre des nombres"""
    try:
        if type(x) is not int and type(x) is not float:
            raise ParametreError("Parametre founis pas correct")
        elif x < 0 :
            raise ValueError("Le nombre ne peut pas être négatif")
        else:
            return x**2
    except Exception as e :
        print(e)
        return 0.0
    
print(calculer_carre.__doc__)
print(calculer_carre(-3))

print("Loading ...")