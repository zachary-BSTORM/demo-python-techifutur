# Programme interactif
"""
Le panier de courses Écrivez un programme avec un menu qui boucle 
jusqu'à ce que l'utilisateur choisisse de quitter.

1. Ajouter un produit
2. Retirer un produit
3. Afficher le panier
4. Vider le panier
5. Quitter
Votre choix :
"""

menu = """
1. Ajouter un produit
2. Retirer un produit
3. Afficher le panier
4. Vider le panier
5. Quitter
"""
panier = {}

stop_app = False

while not stop_app:
    print("==========================================")
    print(menu)
    
    choice = input("Entrez votre choix : ")
    
    match choice:
        case "1":
            key = input("Entrez l'identifiant du produit : ")
            
            name = input("Entrez le nom du produit : ")
            price = float(input("Entrez le prix du produit : "))
            
            panier[key] = {"name":name,"price":price}
            
            
        case "2":
            key = input("Entrez l'identifiant du produit à supprimer : ")
            
            if key in panier.keys():
                del panier[key]
            else:
                print("ce produit n'est pas dans le stock!")
                
                
        case "3":
            for key,value in panier.items():
                print(f"{key} : name : {value["name"]} - price : {value["price"]}€")
            
        case "4":
            panier.clear()
            
        case "5":
            stop_app = True
            
    
    if stop_app == True:
        print("Merci à bientot !")