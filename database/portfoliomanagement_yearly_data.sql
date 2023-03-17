-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: portfoliomanagement
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `yearly_data`
--

DROP TABLE IF EXISTS `yearly_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `yearly_data` (
  `StockID` int NOT NULL,
  `Year` int DEFAULT NULL,
  `average_stock_value` double DEFAULT NULL,
  `outstanding_share` int DEFAULT NULL,
  `yearly_id` int NOT NULL,
  PRIMARY KEY (`yearly_id`),
  KEY `stockID_idx` (`StockID`),
  KEY `yearlyStockID_idx` (`StockID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `yearly_data`
--

LOCK TABLES `yearly_data` WRITE;
/*!40000 ALTER TABLE `yearly_data` DISABLE KEYS */;
INSERT INTO `yearly_data` VALUES (1,2022,57.9032,498,1),(1,2021,57.4256,505,2),(1,2020,38.1175,501,3),(1,2019,30.0182,501,4),(1,2018,27.055,503,5),(1,2017,21.9499,509,6),(1,2016,19.4994,506,7),(1,2015,15.2294,514,8),(1,2014,11.6744,519,9),(1,2013,9.1953,514,10),(1,2012,6.7055,518,11),(1,2011,6.9735,540,12),(1,2010,5.5733,620,13),(1,2009,5.7021,644,14);
/*!40000 ALTER TABLE `yearly_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-17 16:25:00
