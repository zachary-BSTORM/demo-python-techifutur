import json


class Vehicule():
    """
    id
    couleur
    marque
    puissance
    nb_place

    deplacement() : affiche un message
    """
    def __init__(self,id,couleur,marque,puissance,nb_place):
        self.id = id
        self.couleur = couleur
        self.marque = marque
        self.puissance = puissance
        self.nb_place = nb_place
        
    def deplacement(self):
        return "le vehicule se déplace"
    

class Voiture(Vehicule):
    """
    nb_roues
    carburant

    deplacement() : récupère le comportement du parent et ajoute la voiture roule       
    """
    def __init__(self,id,couleur,marque,puissance,nb_place,nb_roues,carburant):
        super().__init__(id,couleur,marque,puissance,nb_place)
        self.nb_roues = nb_roues
        self.carburant = carburant
        
    def deplacement(self):
        print(super().deplacement())
        print("la voiture roule")

    @property
    def carburant(self):
        return self.__carburant

    @carburant.setter
    def carburant(self,value):
        if value in ["diesel","essence"]:
            self.__carburant = value
        else:
            self.__carburant = "inconnu"


class Bateau(Vehicule):
    """
    possede_moteur
    type : "plaisance - peche - sportif"
    
    deplacement() : récupère le comportement du parent et ajoute le bateau navigue
    """
    
    def __init__(self,id,couleur,marque,puissance,nb_place,motor,type_boat):
        super().__init__(id,couleur,marque,puissance,nb_place)
        self.motor = motor
        self.type_boat = type_boat
        
    def deplacement(self):
        print(super().deplacement())
        print("le bateau navigue")

class Concession():
    def __init__(self,name):
        self.name = name
        self.vehicules = dict()
        self.lastId = 0
        
    def ajout_vehicule(self,new_vehicule):
            self.vehicules[self.lastId] = new_vehicule
            self.lastId += 1
            self.save_data()

        
    def remove_vehicule(self,key):
        if key in self.vehicules.keys():
            del self.vehicules[key]
            self.save_data()
        else:
            print("Aucun élément avec cet id ")
        
    
    def show_vehicles(self):
        for k,v in self.vehicules.items():
            if isinstance(v,Voiture):
               print(f"key : {k} : id : {v.id} - couleur : {v.couleur} - marque : {v.marque}  - puissance : {v.puissance} - nb_places : {v.nb_place} - nb_roues : {v.nb_roues} - carburant : {v.carburant}")
            else:
                print(f"key : {k} : id : {v.id} - couleur : {v.couleur} - marque : {v.marque} - puissance : {v.puissance} - nb_places : {v.nb_place} - motor : {v.motor} - type : {v.type_boat}")
                
    def save_data(self):
        with open("data.json" , "w" , encoding="utf-8") as fichier:
           data = [
                    {"categorie": "voiture", "id": e.id, "couleur": e.couleur, "marque": e.marque, "puissance": e.puissance, "nb_place": e.nb_place,"nb_roues": e.nb_roues, "carburant": e.carburant}
                    if isinstance(e, Voiture)
                    else
                    {"categorie": "bateau","id": e.id, "couleur": e.couleur, "marque": e.marque,"puissance": e.puissance, "nb_place": e.nb_place,"motor": e.motor, "type": e.type_boat}
                    for e in self.vehicules.values()]
           json.dump(data , fichier , indent=2,ensure_ascii=False)

    def load_data(self):
        with open("data.json" , "r" , encoding="utf-8") as fichier:
            data = json.load(fichier)
            self.vehicules = { e["id"]: # id valable pour chaque élément
                
                # valeur si vrai suivi de la condition
                Voiture(e["id"], e["couleur"], e["marque"], e["puissance"],e["nb_place"], e["nb_roues"], e["carburant"])   if e["categorie"] == "voiture" 
                     
                # sinon    
                else  
                # valeur si vrai suivi de la condition   
                Bateau(e["id"], e["couleur"], e["marque"], e["puissance"],e["nb_place"], e["motor"], e["type"]) if e["categorie"] == "bateau"
                
                # le _ permet de ne pas traiter la valeur
                else _
                # dans un for on prcours les données
                for e in data 
             }

def get_vehicle():
        type_vehicule = input("Quel type de vehicule voulez-vous ajouter ? b : bateau - v : voiture")
        id = int(input("Entrez l'id du vehicule : "))
        color = input("Entrez la couleur du vehicule : ")
        brand = input("Entrez la marque du vehicule")
        hp = int(input("Entrez la puissance du vehicule : "))
        nb_place = input("Entrez le nombre de place du vehicule : ")
        
        return type_vehicule,id,color,brand,hp,nb_place

menu = """
afficher les vehicules 1
ajouter un vehicule    2
supprimer un vehicule  3
Quitter                4
"""

concession = Concession("ma_concession")

concession.load_data()
while True:
    print("==========================")
    print(menu)
    
    choice = input("Entrez votre choix : ")
    
    match choice:
        case "1":
            concession.show_vehicles()
        
        case "2":
            type_vehicule,id,color,brand,hp,nb_place = get_vehicle()
            
            if type_vehicule == "b":
                motor = input("Est-ce que le bateau possède un moteur ? y - n")
                motor_boat = True if motor == "y" else False
                boat_type = input("Quel est le type du bateau ? plaisance - peche - croisière :")
                
                new_boat = Bateau(id,color,brand,hp,nb_place,motor_boat,boat_type)
                concession.ajout_vehicule(new_boat)
                
                
                
            elif type_vehicule == "v":
                nb_wheels = int(input("Combien de roues possède le vehicule ? "))
                fuel = input("Quel est le type de carburant du vehicule? ")
                new_car = Voiture(id,color,brand,hp,nb_place,nb_wheels,fuel)
                
                concession.ajout_vehicule(new_car)
            else :
                print("Il n'est pas possible d'ajouter d'autres types de vehicules pour le moment")
            
        case "3":
            print("=====================================")
            for k,v in concession.vehicules.items():
                print(f"{k} - {v.marque}")
            print("=====================================")
            
            id_delete = int(input("Quel vehicule voulez-vous supprimez ? "))
            
            concession.remove_vehicule(id_delete)
        case "4":
            break
