class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    _listado = []
    
    def __init__(self,nombre,edad,habitat,genero,zona,colorEscamas,largoCola):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self,color):
        self._colorEscamas = color

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self,largo):
        self._largoCola = largo
    
    def getListado(self):
        return self._listado

    def setListado(self, listado):
        self._listado = listado

    def movimiento(self):
        return "reptar"

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde",3)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco",1)
        