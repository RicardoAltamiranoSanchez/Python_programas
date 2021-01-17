print("Calificaciones")
calificacion=int(input("Digite su calificion"))
if(calificacion ==10 or calificacion == 9 ):
    print("Calificacion A", calificacion)
elif(calificacion ==8 or calificacion == 7 or calificacion == 6):
    print("Regular B",calificacion)
elif(calificacion ==5):
    print("Reprobado F",calificacion)
else:
    print("No existe esa calificacion")