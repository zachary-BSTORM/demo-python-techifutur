# import

# declarations des variables

# methodes

# logique

# Gestion d'utilisateur

# ennoncé
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


def get_value_str(value,name):
    name = input(f"Entrez le {name} : ")
    
    while len(name) < value:
        print(f"Le {name} doit faire au moins {value} caractères")
        name = input(f"Entrez le {name} : ")
    return name
    

def get_number(max,min = 0):
    while True:
        try:
            nb = int(input("Entrez la valeur"))
            
            if min < nb < max:
                return nb

        except:
            print("Veillez entrer une valeur correcte !")

def get_role(*args):
    while True :
        role = input("Entrez un role : user - admin : ")
        
        if role in args:
            return role

def add_user():
    """
    - name : str
    - age  : int
    - adresse : str
    - role : admin | user
    """
    name = get_value_str(3,"name")
    adresse = get_value_str(10,"adresse")
    age = get_number(min=18,max=120)
    role = get_role("user","admin")
    
    list_user[name] = {"name":name,"age":age,"adresse":adresse,"role":role}
    print(f"utilisateur {name} ajouté")

def remove_user(users):
    print("=========================")
    for k in users.keys():
        print(k)
    print("=========================")
    key = get_value_str(2,"nom à supprimer")
    
    del users[key]
    
def update_user(users):
    print("=========================")
    for k in users.keys():
        print(k)
    print("=========================")
    key = input("Quel utilisateur voulez vous modifier ? ")
    
    print(list_user[key])
    name = get_value_str(3,"name")
    adresse = get_value_str(10,"adresse")
    age = get_number(min=18,max=120)
    role = get_role("user","admin")
    
    list_user[name] = {"name":name,"age":age,"adresse":adresse,"role":role}

def show_user(users : dict):
    print("=============================================")
    for k,v in users.items():
        print(f"L'utilisateur : {k} :adresse : {v["adresse"]} - age : {v["age"]} - role : {v["role"]} ")
    print("=============================================")
    


stop_app = False

while not stop_app:
    print(menu)
    
    
    choice = input("Entrez votre choix : ")
    
    match choice :
        case "1":
            show_user(list_user)
        case "2":
           add_user()
        case "3":
            update_user(list_user)
        case "4":
            remove_user(list_user)
        case "5":
            stop_app = True

    if stop_app == True:
        print("Merci à bientot")        