-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.32-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.13.0.7147
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura para tabla db_energia.energy_reading
CREATE TABLE IF NOT EXISTS `energy_reading` (
  `Reading_Id` int(11) NOT NULL AUTO_INCREMENT,
  `voltaje` float DEFAULT NULL,
  `corriente` float DEFAULT NULL,
  `potencia` float DEFAULT NULL,
  `energia` float DEFAULT NULL,
  `Sensor_Id` int(11) DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`Reading_Id`) USING BTREE,
  KEY `Sensor_Id` (`Sensor_Id`),
  CONSTRAINT `FK_reading_sensor` FOREIGN KEY (`Sensor_Id`) REFERENCES `sensor` (`Sensor_Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla db_energia.relay
CREATE TABLE IF NOT EXISTS `relay` (
  `Relay_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Relay_Name` varchar(50) DEFAULT NULL,
  `status` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`Relay_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla db_energia.sensor
CREATE TABLE IF NOT EXISTS `sensor` (
  `Sensor_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Sensor_Names` varchar(50) DEFAULT NULL,
  `Sensortype_Id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Sensor_Id`) USING BTREE,
  KEY `Sensortype_Id` (`Sensortype_Id`),
  CONSTRAINT `FK_sensor_sensor_type` FOREIGN KEY (`Sensortype_Id`) REFERENCES `sensor_type` (`Sensortype_Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla db_energia.sensor_type
CREATE TABLE IF NOT EXISTS `sensor_type` (
  `Sensortype_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Sensor_Names` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Sensortype_Id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla db_energia.temperature_reading
CREATE TABLE IF NOT EXISTS `temperature_reading` (
  `Temperature_Id` int(11) NOT NULL AUTO_INCREMENT,
  `temperatura` float DEFAULT NULL,
  `humedad` float DEFAULT NULL,
  `Sensor_Id` int(11) DEFAULT NULL,
  `fecha` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`Temperature_Id`),
  KEY `Sensor_Id` (`Sensor_Id`),
  CONSTRAINT `FK_temperature_reading_sensor` FOREIGN KEY (`Sensor_Id`) REFERENCES `sensor` (`Sensor_Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla db_energia.user
CREATE TABLE IF NOT EXISTS `user` (
  `User_Id` int(11) NOT NULL,
  `User_Names` varchar(20) NOT NULL,
  `User_Mail` varchar(20) NOT NULL,
  `User_Phone` varchar(20) DEFAULT NULL,
  `User_Name` varchar(20) NOT NULL,
  `User_Password` varchar(20) NOT NULL,
  `Usertype_Id` int(11) DEFAULT NULL,
  `Userstatus_Id` int(11) DEFAULT NULL,
  PRIMARY KEY (`User_Id`),
  KEY `Usertype_Id` (`Usertype_Id`),
  KEY `Userstatus_Id` (`Userstatus_Id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`Usertype_Id`) REFERENCES `user_type` (`Usertype_Id`),
  CONSTRAINT `user_ibfk_2` FOREIGN KEY (`Userstatus_Id`) REFERENCES `user_status` (`Userstatus_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla db_energia.user_status
CREATE TABLE IF NOT EXISTS `user_status` (
  `Userstatus_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Userstatus_Description` varchar(25) NOT NULL,
  PRIMARY KEY (`Userstatus_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla db_energia.user_type
CREATE TABLE IF NOT EXISTS `user_type` (
  `Usertype_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Usertype_Description` varchar(25) NOT NULL,
  PRIMARY KEY (`Usertype_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
