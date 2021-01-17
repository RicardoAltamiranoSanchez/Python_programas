class Persona:
    def __init__ (self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def __str__(self):
        return "El nombre\n"+self.nombre+"El apellido\n"+self.apellido+"La edad\n"+str(self.edad)
    
        