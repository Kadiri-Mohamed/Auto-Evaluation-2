def compute_list_sum(list : list) -> int:
    
    """
        Arg : list des nombres 
        return : int (somme des paires dans la list)
        
        fonction pour calculer la somme des paires dans une list
        
        exemple de list utiliser en arg : [1,4,3,5,2] # Output : 6
    """
    
    somme = 0
    for i in list:
        if i % 2 == 0:
            somme += i
    return somme

print(compute_list_sum([1,4,3,5,2]))
help(compute_list_sum)