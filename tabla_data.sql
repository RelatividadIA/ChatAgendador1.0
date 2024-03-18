
-- Crear la database clientes`
CREATE DATABASE IF NOT EXISTS `crud_clientes`;
USE `crud_clientes`;

-- Crear la tabla `clientes`
CREATE TABLE `clientes` (
  `nombres` varchar(90),
  `apellidos` varchar(90),
  `edad` int,
  `sexo` enum('masculino', 'femenino'),
  `celular` char(10) NOT NULL,  -- Llave primaria
  `email` varchar(255),
  PRIMARY KEY (`celular`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;