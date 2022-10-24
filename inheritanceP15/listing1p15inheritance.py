class Vehicule:
    def avance(self):
        print ("j avance")
class Voiture(Vehicule):
    def __init__(self,model):
        self.model=model
    def printModel(self):
        print (self.model)
v=  Voiture("Espace")
v. avance()
