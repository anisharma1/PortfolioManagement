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
-- Table structure for table `quarterly_data`
--

DROP TABLE IF EXISTS `quarterly_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quarterly_data` (
  `stockID` int NOT NULL,
  `dateMonthYear` tinytext NOT NULL,
  `netIncome` text,
  `sharesOutsanding` int DEFAULT NULL,
  `quarterly_id` int NOT NULL,
  PRIMARY KEY (`quarterly_id`),
  KEY `quarterlyStockID_idx` (`stockID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quarterly_data`
--

LOCK TABLES `quarterly_data` WRITE;
/*!40000 ALTER TABLE `quarterly_data` DISABLE KEYS */;
INSERT INTO `quarterly_data` VALUES (1,'31-12-2022','$241',497,1),(1,'30-09-2022','$294',496,2),(1,'30-06-2022','$307',497,3),(1,'31-03-2022','$284',502,4),(1,'31-12-2021','$260',505,5),(1,'30-09-2021','$288',511,6),(1,'30-06-2021','$341',499,7),(1,'31-03-2021','$298',501,8),(1,'31-12-2020','$225',501,9),(1,'30-09-2020','$264',502,10),(1,'30-06-2020','$241',498,11),(1,'31-03-2020','$203',500,12),(1,'31-12-2019','$203',501,13),(1,'30-09-2019','$150',501,14),(1,'30-06-2019','$174',501,15),(1,'31-03-2019','$247',501,16),(1,'31-12-2018','-$44',503,17),(1,'30-09-2018','$163',502,18),(1,'30-06-2018','$162',502,19),(1,'31-03-2018','$177',507,20),(1,'31-12-2017','$245',509,21),(1,'30-09-2017','$170',510,22),(1,'30-06-2017','$146',505,23),(1,'31-03-2017','$168',511,24),(1,'31-12-2016','-$227',506,25),(1,'30-09-2016','$131',508,26),(1,'30-06-2016','$70',505,27),(1,'31-03-2016','$132',505,28),(1,'31-12-2015','$148',514,29),(1,'30-09-2015','$138',514,30),(1,'30-06-2015','$133',516,31),(1,'31-03-2015','$9',518,32),(1,'31-12-2014','$87',519,33),(1,'30-09-2014','$123',519,34),(1,'30-06-2014','$101',517,35),(1,'31-03-2014','$103',521,36),(1,'31-12-2013','$142',514,37),(1,'30-09-2013','$113',516,38),(1,'30-06-2013','$88',510,39),(1,'31-03-2013','$42',509,40),(1,'31-12-2012','$85',518,41),(1,'30-09-2012','$89',512,42),(1,'30-06-2012','$93',520,43),(1,'31-03-2012','$85',533,44),(1,'31-12-2011','$81',540,45),(1,'30-09-2011','$110',543,46),(1,'30-06-2011','$92',542,47),(1,'31-03-2011','$104',543,48),(1,'31-12-2010','$136',620,49),(1,'30-09-2010','$101',612,50),(1,'30-06-2010','$96',628,51),(1,'31-03-2010','$61',644,52),(1,'31-12-2009','$43',644,53),(1,'30-09-2009','$60',645,54),(1,'30-06-2009','$69',643,55),(1,'31-03-2009','$94',643,56);
/*!40000 ALTER TABLE `quarterly_data` ENABLE KEYS */;
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
