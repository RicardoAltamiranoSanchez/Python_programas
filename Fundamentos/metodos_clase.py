class MiClase:
    
    variable_clase = "Variable clase"
    
    def __init__(self):
        self.variable_instancia = "Variable instancia"
    
    @staticmethod
    def metodo_estatico():
        print("Método estático")
        print(MiClase.variable_clase)
        #Desde un método estático no podemos acceder a una variable de instancia
        #print(MiClase.variable_instancia)
        
    @classmethod
    def metodo_clase(cls):
        print("Método de clase:" + str(cls))  
        print(cls.variable_clase)  
        #No podemos acceder a la variable de instancia desde contexto estático
        #print(cls.variable_instancia)
        
    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print(self.variable_clase)
        print(self.variable_instancia)
            
        
MiClase.metodo_estatico()       
MiClase.metodo_clase() 

print()
objeto1 = MiClase()
objeto1.metodo_instancia()