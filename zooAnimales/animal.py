
class Animal:
    _totalAnimales = 0

    def __init__(self,nombre,edad,habitat,genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self,edad):
        self._edad = edad
    
    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self,habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self,genero):
        self._genero = genero

    def getZona(self):
        return self._zona 

    def setZona(self,zona):
        self._zona = zona

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return "Mamiferos: {}\nAves: {}\nReptiles: {}\nPeces: {}\nAnfibios: {}".format(Mamifero.cantidadMamiferos(),Ave.cantidadAves(),
        Reptil.cantidadReptiles(),Pez.cantidadPeces(),Anfibio.cantidadAnfibios())

    def movimiento(self):
        return "desplazaarse"

    def toString(self):
        return "Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad)+", habito en "+self._habitat + " y mi genero es "+self._genero

