import psycopg2 as bd 
conexion=bd.connect(user='postgres',
                    password='admin',
                    host='127.0.0.1',
                    port='5432',
                    database='prueba')
cursor=conexion.cursor()
bd='SELECT *FROM persona WHERE nombre in %s'
usuarios=input("Ingrese el nombre de los usuario que quiere buscar(al final de cada usuario ponr una coma:)\n")
tupla=tuple(usuarios.split(','))
registros=(tupla,)
cursor.execute(bd,registros)
personas=cursor.fetchall()
for p in personas:
  print(p)
cursor.close()
conexion.close()