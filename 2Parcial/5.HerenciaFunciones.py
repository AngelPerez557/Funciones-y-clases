class  Personaje:
    def __init__(self,nombre,arma):
        self.nombre = nombre
        self.arma = arma

class Mago(Personaje):
    pass

hechicero = Mago("Merlin","Caldero")

print("",hechicero.arma,'\n',hechicero.nombre)