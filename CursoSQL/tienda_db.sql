-------------------------------------
-- Creacion de base de datos tienda
-------------------------------------

CREATE DATABASE tienda_db

-------------------------------------
-- Creacion de la tabla Marca
-------------------------------------

CREATE TABLE marca(
	codigo INT,
	nombre VARCHAR(50)		NOT NULL,
	CONSTRAINT PK_Marca PRIMARY KEY (Codigo)
);

-------------------------------------
-- Creacion de la tabla de producto
-------------------------------------

CREATE TABLE producto(
	codigo INT PRIMARY KEY,
	descripcion varchar(50)		NOT NULL,
	cantidad INT				NOT NULL,
	precio REAL					NOT NULL,
	codigo_marca INT			NOT NULL,
	CONSTRAINT FK_Producto_Marca	FOREIGN KEY	(codigo_marca) REFERENCES marca(codigo)
);

--------------------------------------
-- CONSULTAR PRODUCTO
--------------------------------------
SELECT *FROM MARCA

--------------------------------------
-- INGRESAR DATO
--------------------------------------
INSERT INTO MARCA(CODIGO, NOMBRE) VALUES (001, 'hp')
INSERT INTO MARCA VALUES(002, 'DELL')
INSERT INTO MARCA VALUES(003, 'Asus')
INSERT INTO MARCA VALUES(004, 'Lenovo')
INSERT INTO MARCA VALUES(005, 'Mac')

--------------------------------------
-- ELIMINAR DATO EN MARCA
--------------------------------------
DELETE FROM MARCA WHERE CODIGO = 002

--------------------------------------
-- ELIMINAMOS LA TABLA
--------------------------------------
DROP TABLE PRODUCTO


--------------------------------------
-- ACTUALIZAR UN DATO
--------------------------------------

UPDATE MARCA SET NOMBRE = 'HP' WHERE CODIGO = 001

--------------------------------------
-- CONSULTAR PRODUCTO
--------------------------------------
SELECT *FROM MARCA

--------------------------------------
-- INGRESAR DATO
--------------------------------------

INSERT INTO PRODUCTO VALUES (001, 'Teclado', 10, 20.5, 001)
INSERT INTO PRODUCTO VALUES (002, 'Monitor', 10, 20.5, 002)
INSERT INTO PRODUCTO VALUES (003, 'Raton', 10, 18.5, 003)
INSERT INTO PRODUCTO VALUES (004, 'Camara', 10, 30.3, 004)
INSERT INTO PRODUCTO VALUES (005, 'Audifonos', 10, 10.5, 005)

-- BORRAR SEGUNDO VALOR DE LA TABLA PRODUCTO
-- ACTUALIZAR EL TERCER VALOR DE LA TABLA MARCA
-- CONSULTAR LA TABLA PRODUCTO
-- CONSULTAR LA TABLA MARCA