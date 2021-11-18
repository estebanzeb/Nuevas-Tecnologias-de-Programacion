-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-10-2021 a las 04:44:30
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `invoice`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `invoice`
--

CREATE TABLE customer(
	id int unsigned auto_increment primary key,
	name varchar(25) NOT NULL,
  status enum('Activo','Inactivo') NOT NULL,
  mobile varchar(25) NOT NULL
);


INSERT INTO `customer` (`id`, `name`, `status`, `mobile`) VALUES
(1, 'Test Up', 'Activo', '+57 314 6958876'),
(2, 'Daniel Sanchez Z' , 'Activo' , '+57 314 6958876');

CREATE TABLE invoice(
	id int unsigned auto_increment primary key,
	number varchar(25) NOT NULL,
    date date NOT NULL,
    id_user int unsigned,
    foreign key(id_user) references customer(id),
    price varchar(25) NOT NULL,
    balance varchar(25) NOT NULL
);

--
-- Volcado de datos para la tabla `invoice`
--

INSERT INTO `invoice` (`id`,  `number`, `date`, `id_user`, `price`, `balance`) VALUES
(1, 121212, '2021-10-16', 1, 4000, 4000),
(5, 232323, '2021-10-14', 2, 80000, 80000);

-- --------------------------------------------------------
CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(3) NOT NULL 
);


INSERT INTO `user` (`id`,  `name`, `email`, `password`) VALUES
(1, 'Esteban', 'estebanzeb@gmail.com', '123'),
(2, 'Esteban2', 'estebanzeb2@gmail.com', '123');
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--


--
-- Volcado de datos para la tabla `user`
--


--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_customer` (`id_customer`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `invoice`
--
ALTER TABLE `invoice`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=232325;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `invoice`
--
ALTER TABLE `invoice`
  ADD CONSTRAINT `invoice_ibfk_1` FOREIGN KEY (`id_customer`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;