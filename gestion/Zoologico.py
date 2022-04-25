class Zoologico:

    def __init__(self,nombre,ubicacion,zonas):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    
    def getZonas(self):
        return self._zonas

    def setZonas(self,zonas):
        self._zonas = zonas

    def cantidadTotalAnimales(self):
        total = 0
        for zona in self._zonas:
            total += zona.cantidadAnimales()

        return total

    def agregarZonas(self,zona):
        self._zonas.append(zona)
        
