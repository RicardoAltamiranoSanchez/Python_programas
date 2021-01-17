import psycopg2 as bd
conexion=bd.connect(user='postgres',
                    password='admin',
                    host='127.0.0.1',
                    port='5432',
                    database='prueba')
cursor=conexion.cursor()
setencia='INSERT INTO persona(nombre,apellido,correo) VALUES (%s,%s,%s);'

while True:
    salir=input("Quiere salir del programa s/n\n")
    salir.lower()
    if(salir=="n"):
       nombre=input("Digite el nombre\n")
       apellido=input("Digite el apellido\n")
       correo=input("Digite el correo\n")
       tupla=((nombre,apellido,correo),
              (nombre,apellido,correo),
              (nombre,apellido,correo))
    elif(salir=="s"):
        break
    else:
        print("Error esa opcion no existe")

cursor.executemany(setencia,tupla)
conexion.commit()
contar_registros=cursor.rowcount

print(f'Numero de registros ingresado:{contar_registros}')
setencia2='SELECT *FROM persona;'
cursor.execute(setencia2)
personas=cursor.fetchall()
for p in personas:
    print(p)

cursor.close()
conexion.close()              
    