from figura import Figura
from color import Color
class Rectangulo(Figura,Color):
    def __init__(self,base,altura,color):
        Figura.__init__(self,base,altura)
        Color.__init__(self,color)
    def Area(self):
        return self.getAltura()*self.getBase()
    def __str__(self):
        return "Base "+str(self.getBase())+"Altura "+str(self.getAltura())+"Color"+self.getColor()
        
    