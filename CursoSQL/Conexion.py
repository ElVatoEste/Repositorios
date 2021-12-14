import psycopg2

conexion = psycopg2.connect(database = "postgres", user = "postgres", password = "1234", host="localhost", puerto=5432)

print("Conexcion exitosa")