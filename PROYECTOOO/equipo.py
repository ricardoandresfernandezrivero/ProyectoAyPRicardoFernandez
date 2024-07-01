#Clase equipo
class Equipo:
    def __init__(self,codigofifa,nombre,grupo):
        self.codigofifa=codigofifa
        self.nombre=nombre
        self.grupo=grupo
    def show(self):
        return {"codigo":self.codigofifa, "nombre":self.nombre, "grupo":self.grupo}