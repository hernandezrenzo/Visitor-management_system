-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 18, 2021 at 09:57 AM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vvms-tkinter`
--
CREATE DATABASE IF NOT EXISTS `vvms-tkinter` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `vvms-tkinter`;

-- --------------------------------------------------------

--
-- Table structure for table `vvms`
--

DROP TABLE IF EXISTS `vvms`;
CREATE TABLE IF NOT EXISTS `vvms` (
  `lbl_id` int(11) NOT NULL AUTO_INCREMENT,
  `lbl_name` varchar(256) NOT NULL,
  `lbl_age` varchar(100) NOT NULL,
  `lbl_gndr` varchar(100) NOT NULL,
  `lbl_adres` varchar(256) NOT NULL,
  `lbl_cntct` varchar(100) NOT NULL,
  `lbl_plt` varchar(100) NOT NULL,
  `lbl_hnv` varchar(256) NOT NULL,
  `lbl_date` date NOT NULL,
  `lbl_in` varchar(100) NOT NULL,
  `lbl_out` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`lbl_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vvms`
--

INSERT INTO `vvms` (`lbl_id`, `lbl_name`, `lbl_age`, `lbl_gndr`, `lbl_adres`, `lbl_cntct`, `lbl_plt`, `lbl_hnv`, `lbl_date`, `lbl_in`, `lbl_out`) VALUES
(5, 'Mikaela Plata', '20', 'Female', 'Mahabang Parang, Batangas', '09228743521', 'ASX 331', '015 Knight Street, Alangilan Batangas City', '2021-12-01', '12:00 PM', ''),
(4, 'Zoey Cometa', '18', 'Female', 'Bauan, Batangas', '09440129588', 'ZXC 441', '050 Rook Street, Alangilan Batangas City', '2021-12-01', '10:00 AM', ''),
(3, 'James Dela Cruz', '30', 'Male', 'Lemery, Batangas', '09294512123', 'KFC 111', '011 Bishop Street, Alangilan Batangas City', '2021-12-01', '7:00 AM', ''),
(6, 'Justin Morales', '25', 'Male', 'Kumintang Ibaba Batangas City', '09195551247', 'TVX 661', '05 Pawn Street, Alangilan Batangas City', '2021-12-12', '1:42 PM', ''),
(2, 'Leonalyn Abcede', '21', 'Female', 'San Juan, Batangas', '09281652354', 'TYU 664', '101 Queen Street, Alangilan Batangas City', '2021-11-30', '10:00 PM', ''),
(1, 'Spencer Ramirez', '25', 'Male', 'San Jose, Batangas', '09192158475', 'QWE 123', '111 King Street, Alangilan Batangas City', '2021-11-30', '9:58 PM', '9:50 AM');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
