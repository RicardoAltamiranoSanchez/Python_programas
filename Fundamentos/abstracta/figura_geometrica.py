#ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    @abstractmethod
    def area(self):
       raise NotImplementedError("Método area() no implementado")
       