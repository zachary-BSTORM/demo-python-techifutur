

def afficher_liste(value,liste = None):
    if liste is None:
        liste= []

    liste.append(value)
    return liste
    
ma_liste = []
print(afficher_liste(1)) # [1]
print(afficher_liste(2)) # [1,2]