class Figura():
    def __init__(self,altura,base):
        self.__altura=altura
        self.__base=base
    def __str__(self):
        return "Altura "+str(self.__altura)+" Base "+str(self.__base)
    def getAltura(self):
        return self.__altura
    def setAltura(self,valor):
        self.__altura=valor
    def getBase(self):
        return self.__base
    def setBase(self,valor):
        self.__base=base
   
            