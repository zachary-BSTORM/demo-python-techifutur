list_dict = dict()

menu = """
afficher les taches  1
ajouter une tache    2
supprimer une tache  3
Quitter              4
"""

continue_app = True


while continue_app:
    print(menu)
    
    choice = input("Entrez votre choix")
    
    match choice :
        case "1":
            for k,v in list_dict.items():
                print(f"la tache : {k} - titre : {v["title"]} - description : {v["description"]}")
        case "2":
            key = input("Entrez la clé de l'élément : ")
            
            title = input("Entrez lz titre de la tache : ")
            description = input("Entrez la description de la tache : ")
            
            list_dict[key] = {"title":title,"description":description}
        case "3":
            id = input("Entrez la clé de l'élément à supprimer : ")
            del list_dict[id]
        case "4":
            pass    