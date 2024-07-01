#Clase entrada y clases hijas VIP  y normal
class Entrada:
    def __init__(self,cedula,partido,id):
        self.cedula = cedula
        self.partido = partido
        self.id = id
        self.asiento = []
        self.usada = False
        self.total = None
    def show(self):
        return {"cedula":self.cedula, "partido":self.partido, "tipo":self.tipo, "id":self.id, "asiento": self.asiento, "usada":self.usada, "total":self.total}
    
class VIP(Entrada):
    def __init__(self,cedula,partido,id):
        super().__init__(cedula,partido,id)
        self.tipo = "Normal"
    def show(self):
        return {"cedula":self.cedula, "partido":self.partido, "tipo":self.tipo, "id":self.id, "asiento": self.asiento, "usada":self.usada, "total":self.total}
    
class Normal(Entrada):
    def __init__(self,cedula,partido,id):
        super().__init__(cedula,partido,id)
        self.tipo = "VIP"
    def show(self):
        return {"cedula":self.cedula, "partido":self.partido, "tipo":self.tipo, "id":self.id, "asiento": self.asiento, "usada":self.usada, "total":self.total}
