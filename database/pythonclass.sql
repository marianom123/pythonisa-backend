-- --------------------------------------------------------
-- Host:                         sql10.freemysqlhosting.net
-- Versión del servidor:         5.5.62-0ubuntu0.14.04.1 - (Ubuntu)
-- SO del servidor:              debian-linux-gnu
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para sql10717628
CREATE DATABASE IF NOT EXISTS `sql10717628` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `sql10717628`;

-- Volcando estructura para tabla sql10717628.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(50) NOT NULL DEFAULT 'titulo_de_producto',
  `descripcion` varchar(500) NOT NULL DEFAULT 'descripcion_de_producto',
  `precio` float(10,2) NOT NULL DEFAULT '0.00',
  `foto` varchar(5000) NOT NULL DEFAULT 'messi2.jpeg',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla sql10717628.productos: ~2 rows (aproximadamente)
INSERT INTO `productos` (`id`, `titulo`, `descripcion`, `precio`, `foto`) VALUES
	(18, 'messi 32', 'prueba', 123.04, '20240707_023636_producto22.png'),
	(20, 'Pulover', 'pulover VERDE de verano', 4500.78, '20240707_023624_producto30.png');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
