from forma import Forma 

class Quadrado(Forma):
    def __init__(self,nome,lado):
        super().__init__(nome)
        self.lado = lado

    def calculaArea(self,lado):
        return lado * lado
    
    def __str__(self):
        return f"{super().__str__()}com media de lado = {self.lado}"

    


