import  psycopg2 as bd
conexion=bd.connect(user='postgres',
                    password='admin',
                    host='127.0.0.1',
                    port='5432',
                    database='prueba')
cursor=conexion.cursor()
setencia='UPDATE persona set nombre=%s,apellido=%s,correo=%s where nombre=%s;'
tupla=('uriel1','urrita2','uriel@gmail.com','Ricardo')
cursor.execute(setencia,tupla)
conexion.commit()
setencia2='SELECT DISTINCT *FROM persona ORDER BY nombre ASC  ;'
conteo=cursor.rowcount
cursor.execute(setencia2)
personas=cursor.fetchall()
print(f'Registro actualizado:{conteo}')
for p in personas:
    print(p)

conexion.close()
cursor.close()    