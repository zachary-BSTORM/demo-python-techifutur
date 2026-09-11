class Animal():
    def __init__(self,nom : str,age : int,couleur : str):
        self.nom = nom
        self._age = age
        self.couleur = couleur
        
        
    @property
    def couleur(self):
        return self.__couleur
    
    @couleur.setter
    def couleur(self,value):
        if value is not None:
            if len(value) < 3:
                print("le nom doit faire au minimum 3 caractères")
            else:
                self.__couleur = value
        
    def faire_du_bruit(self):
        print("l'animal fait du bruit")

class Chat(Animal):
    """
    la classe chat récupère son comportement de son parent : Animal
    """
    
    def __init__(self,nom,age,croquettes,couleur):
        super().__init__(nom,age,couleur)
        self.croquettes = croquettes
        
    def faire_du_bruit(self):
        super().faire_du_bruit()
        print("miaou du chat")

class Chaton(Chat):
    """
    ici la classe chaton récupère faire du bruit de son parent le plus proche : Chat
    """
    def __init__(self,jouet,nom,age,croquettes,couleur):
        super().__init__(nom,age,croquettes,couleur)
        self.jouet = jouet
    
    pass


class Animalerie():
    def __init__(self,nom):
        self.nom = nom
        self.animaux = []

    def ajouter_animal(self,new_animal):
        self.animaux.append(new_animal)
        
        
    def liste_animaux(self):
        for a in self.animaux:
            if isinstance(a,Chaton):
                print(f" l'animal {a.nom} - age {a._age} - couleur {a.couleur} - jouet {a.jouet}")
            else:
                print(f" l'animal {a.nom} - age {a._age} - couleur {a.couleur}")

# ===========================================================================
rex = Animal("rex",8,"noi et brun")
garfield = Chat("garfield",5,"whiskas","roux")
mini_garfield = Chaton("pelotte de laine","bébé garfield",1,"whiskas","roux")

tom_and_co = Animalerie("animalerie")


tom_and_co.ajouter_animal(rex)
tom_and_co.ajouter_animal(garfield)
tom_and_co.ajouter_animal(mini_garfield)

tom_and_co.liste_animaux()
