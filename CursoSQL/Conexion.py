import psycopg2

conexion = psycopg2.connect(database="prueba", user="postgres", password="1234", host="localhost", port="5432")

print("Conexion exitosa")


cursor = conexion.cursor()

# cursor.execute("UPDATE estudiante SET nombre = 'Andreh Gomez' where id = '2021' ")
# conexion.commit()

cursor.execute("SELECT id, nombre, edad, email FROM estudiante")
rows = cursor.fetchall()

for row in rows:
    print("\nid=", row[0])
    print("nombre =", row[1])
    print("edad =", row[2])
    print("email =", row[3], "\n")

print("Total de actualizaciones =", cursor.rowcount)

# cursor.execute("DELETE FROM ESTUDIANTE WHERE id = '2021'")

#cursor.execute("INSERT INTO estudiante (id,nombre,edad,email) VALUES (2021, 'Andres Gomez', 16, 'AndrGom@gmail.com')")
#print("Ingreso de datos exitoso")


conexion.commit()
conexion.close

#cursor.execute('''CREATE TABLE estudiante(
#                    id VARCHAR(9) PRIMARY KEY,
 #                   nombre VARCHAR(50),
  #                  edad INTEGER,
   #                 email VARCHAR(50));''')

# print("Tabla exitosamente creada")

