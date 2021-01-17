import psycopg2 as bd
conexion=bd.connect(user='postgres',
                    password='admin',
                    host='127.0.0.1',
                    port='5432',
                    database='prueba')

cursor=conexion.cursor()
setencia='UPDATE persona SET nombre=%s,apellido=%s,correo=%s where nombre=%s;'
tupla=(('alfredo','Rodriguez','alfredo@gmail.com','Rodrigo'),
       ('jose juan','Mendoza','josejuan@gmail.com','Gabriela'))
cursor.executemany(setencia,tupla)
conexion.commit()
conteo=cursor.rowcount
print(f"atos actualizado en toda:{conteo}")
sentencia2='SELECT*FROM persona order by nombre asc;'
cursor.execute(sentencia2)
personas=cursor.fetchall()
for p in personas:
    print(p)