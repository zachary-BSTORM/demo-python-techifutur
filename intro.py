class Animal():
    def __init__(self,nom : str,age : int,couleur : str):
        self.nom = nom
        self.couleur = couleur
        
    @property
    def couleur(self):
        return self.__couleur
    
    @couleur.setter
    def couleur(self,value):
        self.__couleur = value
        
    def faire_du_bruit(self):
        print("l'animal fait du bruit")
        
        

animal_1 = Animal("garfield",5,"roux")

print(animal_1.couleur)
print(animal_1._Animal__couleur)

