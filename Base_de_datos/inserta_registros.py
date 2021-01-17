import psycopg2 as bd
conexion=bd.connect(user='postgres',
                    password='admin',
                    host='127.0.0.1',
                    port='5432',
                    database='prueba')
cursor=conexion.cursor()
setencia='INSERT INTO persona (nombre,apellido,correo) VALUES (%s,%s,%s);'
nombre=input("Ingrese el nombre\n")
apellido=input("Ingrese el apellido\n")
correo=input("Ingrese el correo\n")
nueva_persona=(nombre,apellido,correo)
cursor.execute(setencia,nueva_persona)

conexion.commit()
registros_insertados=cursor.rowcount
print(registros_insertados)
setencia2='SELECT *FROM persona;'
cursor.execute(setencia2)
personas=cursor.fetchall()
for p in personas:
    print(p)
conexion.close()
cursor.close()