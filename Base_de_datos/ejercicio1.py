import psycopg2 as bd
conexion=bd.connect(user='postgres',
                    password='admin',
                    host='127.0.0.1',
                    port='5432',
                    database='prueba')

cursor=conexion.cursor()
variable='SELECT *FROM  persona WHERE nombre=%s;'
id=input('Digite el nombre de la persona que desea buscar\n')
persona=(id,)
cursor.execute(variable,persona)
registro=cursor.fetchone()
print(registro)
cursor.close()
conexion.close()
