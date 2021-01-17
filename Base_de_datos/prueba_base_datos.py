import psycopg2
conexion = psycopg2.connect(user='postgres',
               password='admin',
               host='127.0.0.1', 
               port='5432',
               database='prueba')
cursor=conexion.cursor()
pedir='SELECT *FROM persona;'
cursor.execute(pedir)
registros=cursor.fetchall()
print(registros)
conexion.close()
cursor.close()
