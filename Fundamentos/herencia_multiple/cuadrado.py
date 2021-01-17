from figura import Figura
from color import Color
class Cuadrado(Figura,Color):
    def __init__(self,lado,color):
        Figura.__init__(self,lado,lado)
        Color.__init__(self,color)
    def Area(self):
        return self.getAltura()*self.getBase()
    def __str__(self):
        return "Lado "+str(self.getAltura())+" color "+self.getColor()

        