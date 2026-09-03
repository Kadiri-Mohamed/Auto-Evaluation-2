def diviser(a,b):
    """Diviser 2 nombres et return result"""
    try:
        return a/b

    except ZeroDivisionError:
        print("peut pas diviser par 0")
        return 0.0
    except TypeError:
        print("division just pour les int")
        return 0.0
    finally :
        print("Operation terminee.")
print(diviser.__doc__)
print(diviser(5,2))
print(diviser(1,0))
print(diviser(1,"3"))
    
    
    

    
