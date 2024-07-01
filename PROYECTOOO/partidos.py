#Clase partido
class Partido:
    def __init__(self,equipolocal,equipovisitante,fecha,estadio):
        self.equipolocal = equipolocal
        self.equipovisitante = equipovisitante
        self.fecha = fecha
        self.estadio = estadio
    def show(self):
        return {"local":self.equipolocal, "visitante":self.equipovisitante, "fecha":self.fecha,"estadio":self.estadio}