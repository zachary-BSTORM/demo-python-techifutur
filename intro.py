
ma_liste = [1,2,3,4,5,6]

try:
    
    index = int(input("Entrez l'index de l'élément à modifier : "))
    new_value = int(input("Entrez la nouvelle valeur : "))
    ma_liste[index] = new_value
    
except ValueError:
    print("La valeur est incorrect")
except IndexError:
    print("L'index n'existe pas dans la liste")
except:
    print("autre erreur")
else:
    for v in ma_liste:
        print(v)
