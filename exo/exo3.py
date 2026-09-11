# import

# declarations des variables

# methodes

# logique

# Gestion d'utilisateur

"""
les utilisateurs sont dans un dict

"model" : 
    - name
    - age
    - adresse
    - role : admin | user

methodes : 
    - add_user()
    - remove_user()
    - update_user()
    - show_user()
    
    - get_name() : le nom doit faire au moins 3 caractère
    - get_number() : récupération de l'age : l'age doit faire au minimum 18 et maximum 120
    - get_role() : le role doit être : admin | user

- Programme interactif 
    - affichage du menu 
    - récupération du choix 
    - execution
"""

list_user = dict()

menu = """
Afficher liste        : 1
Ajouter utilisateur   : 2
Modifier utilisateur  : 3
Supprimer utilisateur : 4
Quitter               : 5
"""


def get_name():
    pass

def get_number():
    pass

def get_role():
    pass

def add_user(users):
    pass

def remove_user(users):
    pass

def update_user(users,updated_users):
    pass

def show_user(users):
    pass


stop_app : False

while not stop_app:
    print(menu)
    
    choice = input("Entrez votre choix : ")
    
    match choice :
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass