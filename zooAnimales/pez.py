#from animal import Animal


class Pez(Animal):
    salmones = 0
    bacalaos = 0
    _listado = []
    
    def __init__(self,nombre,edad,habitat,genero,zona,colorEscamas,cantidadAletas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self,color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self,cantidad):
        self._cantidadAletas = cantidad

    def getListado(self):
        return self._listado

    def setListado(self, listado):
        self._listado = listado

    def movimiento(self):
        return "nadar"

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo",6)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris",6)
        