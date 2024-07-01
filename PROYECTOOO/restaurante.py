#Clase restaurant
class Restaurant:
    def __init__(self,estadio,nombre,productos):
        self.estadio = estadio
        self.nombre = nombre
        self.productos = productos

    def show(self):
        return {"estadio":self.estadio, "nombre":self.nombre, "productos":self.productos}
