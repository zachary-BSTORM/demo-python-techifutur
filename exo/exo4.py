# Classe Vehicule
"""
id
couleur
marque
puissance
nb_place

deplacement() : affiche un message
"""


# Classe Voiture
"""
nb_roues
carburant

deplacement() : récupère le comportement du parent et ajoute la voiture roule
"""

# Classe Bateau
"""
possede_moteur
type : "plaisance - peche - sportif"
deplacement() : récupère le comportement du parent et ajoute le bateau navigue
"""


# Classe concession
"""
nom
list_vehicule = dict()


ajout_vehicule()
suppression_vehicule()

"""

class MaClasse():
    def __init__(self,prop1):
        self.prop1 = prop1
        
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value 
    
        
        
        
obj_1 = MaClasse("info 1")