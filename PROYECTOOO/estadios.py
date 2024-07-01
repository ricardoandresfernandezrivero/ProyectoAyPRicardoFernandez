#Clase estadio
class Estadio:
    def __init__(self,nombre,ubicacion,id):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.id = id
    def show(self):
        return {"nombre":self.nombre, "ubicacion":self.ubicacion, "id":self.id}