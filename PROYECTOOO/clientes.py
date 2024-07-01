#Clase cliente
class Cliente:
    def __init__(self,nombrecliente,cedula,edad,partidoquevera,tipo):
        self.nombrecliente = nombrecliente
        self.cedula = cedula
        self.edad = edad
        self.partidoquevera = partidoquevera
        self.tipo = tipo
        self.productos = []

    def show(self):
        return {"nombre":self.nombrecliente, "cedula":self.cedula, "edad":self.edad, "partido":self.partidoquevera, "tipo":self.tipo, "productos": []}
    