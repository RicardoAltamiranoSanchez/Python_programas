import psycopg2 as bd
conexion=bd.connect(user='postgres',
                    password='admin',
                    host='127.0.0.1',
                    port='5432',
                    database='prueba')
cursor=conexion.cursor()
try:
    setencia1='INSERT INTO persona(nombre,apellido,correo) VALUES(%s,%s,%s);'
    insertar=('Ricardo','Altamirano','ricardo@gamil.com')
    cursor.execute(setencia1,insertar)
    setencia2='SELECT *FROM persona;'
    cursor.execute(setencia2)
    personas=cursor.fetchall()
    for p in personas:
        print(p)
except Exception as e:
    conexion.rollback()
    print(f"Errror {e}") 
    
finally:
    cursor.close() 
    conexion.close()
       
           

