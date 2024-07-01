#Clase producto y clases hijas alimento y bebida
class Producto:
    def __init__(self,nombre,cantidad,precio,restaurante):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.restaurante = restaurante
class Alimento(Producto):
    def __init__(self,nombre,cantidad,precio,tipo,restaurante):
        super().__init__(nombre,cantidad,precio,restaurante)
        self.tipo = tipo
    def show(self):
        return {"nombre":self.nombre, "cantidad":self.cantidad, "precio":self.precio, "tipo":self.tipo, "restaurante":self.restaurante}

class Bebidas(Producto):
    def __init__(self,nombre,cantidad,precio,tipo,restaurante):
        super().__init__(nombre,cantidad,precio,restaurante)
        self.tipo = tipo
    def show(self):
        return {"nombre":self.nombre, "cantidad":self.cantidad, "precio":self.precio, "tipo":self.tipo, "restaurante":self.restaurante}