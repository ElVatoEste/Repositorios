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



SELECT *FROM MARCA

