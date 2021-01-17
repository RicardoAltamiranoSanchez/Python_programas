import psycopg2 as bd
conexion=bd.connect(user='postgres',
                    password='admin',
                    host='127.0.0.1',
                    port='5432',
                    database='prueba')
cursor=conexion.cursor()
setencia='DELETE FROM persona WHERE nombre=%s;'

tupla=(("Fabian",),
       ("Batman",),
       ("alfredo",))

cursor.executemany(setencia,tupla)
conexion.commit()
conteo=cursor.rowcount
print(f"Registros eliminados:{conteo}")
sentecia2='SELECT*FROM persona;'
cursor.execute(sentecia2)
personas=cursor.fetchall()
for p in personas:
    print(p)
    