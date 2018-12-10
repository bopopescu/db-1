-- phpMyAdmin SQL Dump
-- version 4.4.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Oct 05, 2018 at 08:24 AM
-- Server version: 5.6.26
-- PHP Version: 5.6.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db-project-1`
--

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE IF NOT EXISTS `department` (
  `Name` varchar(50) NOT NULL,
  `Number` int(11) NOT NULL DEFAULT '0',
  `Locations` int(11) DEFAULT NULL,
  `Manager` varchar(100) DEFAULT NULL,
  `Manager_start_date` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `dependent`
--

CREATE TABLE IF NOT EXISTS `dependent` (
  `Employee` varchar(15) NOT NULL,
  `Dependent_name` varchar(200) DEFAULT NULL,
  `Sex` varchar(5) DEFAULT NULL,
  `Birth_date` varchar(25) DEFAULT NULL,
  `Relationship` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `dept_locations`
--

CREATE TABLE IF NOT EXISTS `dept_locations` (
  `Name` varchar(50) NOT NULL,
  `Number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE IF NOT EXISTS `employee` (
  `Fname` varchar(50) NOT NULL,
  `SSN` varchar(15) NOT NULL,
  `Address` varchar(500) DEFAULT NULL,
  `Sex` varchar(6) DEFAULT NULL,
  `Supervisor` varchar(100) DEFAULT NULL,
  `Minit` varchar(1) DEFAULT NULL,
  `Lname` varchar(50) NOT NULL,
  `Department` int(11) DEFAULT NULL,
  `Birth_date` varchar(12) DEFAULT NULL,
  `Salary` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

CREATE TABLE IF NOT EXISTS `project` (
  `Name` varchar(50) NOT NULL,
  `Number` int(11) NOT NULL,
  `Location` varchar(25) DEFAULT NULL,
  `Controlling_department` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `works_on`
--

CREATE TABLE IF NOT EXISTS `works_on` (
  `SSN` varchar(15) DEFAULT NULL,
  `Project` int(11) DEFAULT NULL,
  `Hours` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`Number`),
  ADD UNIQUE KEY `Name` (`Name`),
  ADD KEY `FK_Locations` (`Locations`),
  ADD KEY `FK_PersonOrder` (`Manager`);

--
-- Indexes for table `dependent`
--
ALTER TABLE `dependent`
  ADD KEY `FK_EmployeeSSN` (`Employee`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`SSN`),
  ADD KEY `FK_DepartmentNumber` (`Department`),
  ADD KEY `FK_Supervisor` (`Supervisor`);

--
-- Indexes for table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`Number`),
  ADD UNIQUE KEY `Name` (`Name`),
  ADD KEY `FK_DEPARTMENT` (`Controlling_department`);

--
-- Indexes for table `works_on`
--
ALTER TABLE `works_on`
  ADD KEY `FK_Project` (`Project`),
  ADD KEY `FK_WORKS_ON` (`SSN`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `department`
--
ALTER TABLE `department`
  ADD CONSTRAINT `FK_PersonOrder` FOREIGN KEY (`Manager`) REFERENCES `employee` (`SSN`);

--
-- Constraints for table `dependent`
--
ALTER TABLE `dependent`
  ADD CONSTRAINT `FK_EmployeeSSN` FOREIGN KEY (`Employee`) REFERENCES `employee` (`SSN`);

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `FK_DepartmentNumber` FOREIGN KEY (`Department`) REFERENCES `department` (`Number`),
  ADD CONSTRAINT `FK_Supervisor` FOREIGN KEY (`Supervisor`) REFERENCES `employee` (`SSN`);

--
-- Constraints for table `project`
--
ALTER TABLE `project`
  ADD CONSTRAINT `FK_DEPARTMENT` FOREIGN KEY (`Controlling_department`) REFERENCES `department` (`Number`);

--
-- Constraints for table `works_on`
--
ALTER TABLE `works_on`
  ADD CONSTRAINT `FK_Project` FOREIGN KEY (`Project`) REFERENCES `project` (`Number`),
  ADD CONSTRAINT `FK_WORKS_ON` FOREIGN KEY (`SSN`) REFERENCES `employee` (`SSN`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
