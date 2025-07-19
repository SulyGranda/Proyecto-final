CREATE DATABASE reserva;
GO

USE reserva;
GO

CREATE TABLE reservas (
    id INT IDENTITY(1,1) PRIMARY KEY,
    cedula NVARCHAR(10) NOT NULL UNIQUE,
    nombre NVARCHAR(50) NOT NULL,
    departamento NVARCHAR(50) NOT NULL,
    email NVARCHAR(100) NOT NULL,
    sala NVARCHAR(50) NOT NULL,
    fecha DATE NOT NULL,
    hora_inicio NVARCHAR(5) NOT NULL,
    hora_fin NVARCHAR(5) NOT NULL
);
GO

