class Rectangulo:
    
    #Calcular la area de un rectangulo
    def _init_(self , altura,base):
        self.altura=altura
        self.base=base
    def area(self):
        return self.base*self.altura

resu=Rectangulo(20,30)
