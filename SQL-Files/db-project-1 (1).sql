-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 04, 2018 at 01:06 PM
-- Server version: 5.7.23-0ubuntu0.16.04.1
-- PHP Version: 7.0.32-0ubuntu0.16.04.1

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
-- Table structure for table `DEPARTMENT`
--

CREATE TABLE `DEPARTMENT` (
  `Name` varchar(50) NOT NULL,
  `Number` int(11) NOT NULL,
  `Locations` int(11) DEFAULT NULL,
  `Manager` varchar(100) DEFAULT NULL,
  `Manager_start_date` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `DEPENDENT`
--

CREATE TABLE `DEPENDENT` (
  `Employee` varchar(15) NOT NULL,
  `Dependent_name` varchar(200) DEFAULT NULL,
  `Sex` varchar(5) DEFAULT NULL,
  `Birth_date` varchar(25) DEFAULT NULL,
  `Relationship` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `DEPT_LOCATIONS`
--

CREATE TABLE `DEPT_LOCATIONS` (
  `Name` varchar(50) NOT NULL,
  `Number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `EMPLOYEE`
--

CREATE TABLE `EMPLOYEE` (
  `Fname` varchar(50) NOT NULL,
  `SSN` varchar(15) NOT NULL,
  `Address` varchar(500) DEFAULT NULL,
  `Sex` varchar(6) DEFAULT NULL,
  `Supervisor` varchar(100) DEFAULT NULL,
  `Minit` varchar(1) NOT NULL,
  `Lname` varchar(50) NOT NULL,
  `Department` int(11) DEFAULT NULL,
  `Birth_date` varchar(12) DEFAULT NULL,
  `Salary` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `PROJECT`
--

CREATE TABLE `PROJECT` (
  `Name` varchar(50) NOT NULL,
  `Number` int(11) NOT NULL,
  `Location` varchar(25) DEFAULT NULL,
  `Controlling_department` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `WORKS_ON`
--

CREATE TABLE `WORKS_ON` (
  `SSN` varchar(15) DEFAULT NULL,
  `Project` int(11) DEFAULT NULL,
  `Hours` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `DEPARTMENT`
--
ALTER TABLE `DEPARTMENT`
  ADD PRIMARY KEY (`Number`),
  ADD UNIQUE KEY `Name` (`Name`),
  ADD KEY `FK_Locations` (`Locations`),
  ADD KEY `FK_PersonOrder` (`Manager`);

--
-- Indexes for table `DEPENDENT`
--
ALTER TABLE `DEPENDENT`
  ADD KEY `FK_EmployeeSSN` (`Employee`);

--
-- Indexes for table `DEPT_LOCATIONS`
--
ALTER TABLE `DEPT_LOCATIONS`
  ADD PRIMARY KEY (`Number`),
  ADD UNIQUE KEY `Name` (`Name`);

--
-- Indexes for table `EMPLOYEE`
--
ALTER TABLE `EMPLOYEE`
  ADD PRIMARY KEY (`SSN`),
  ADD KEY `FK_DepartmentNumber` (`Department`),
  ADD KEY `FK_Supervisor` (`Supervisor`);

--
-- Indexes for table `PROJECT`
--
ALTER TABLE `PROJECT`
  ADD PRIMARY KEY (`Number`),
  ADD UNIQUE KEY `Name` (`Name`),
  ADD KEY `FK_DEPARTMENT` (`Controlling_department`);

--
-- Indexes for table `WORKS_ON`
--
ALTER TABLE `WORKS_ON`
  ADD KEY `FK_Project` (`Project`),
  ADD KEY `FK_WORKS_ON` (`SSN`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `DEPARTMENT`
--
ALTER TABLE `DEPARTMENT`
  ADD CONSTRAINT `FK_Locations` FOREIGN KEY (`Locations`) REFERENCES `DEPT_LOCATIONS` (`Number`),
  ADD CONSTRAINT `FK_PersonOrder` FOREIGN KEY (`Manager`) REFERENCES `EMPLOYEE` (`SSN`);

--
-- Constraints for table `DEPENDENT`
--
ALTER TABLE `DEPENDENT`
  ADD CONSTRAINT `FK_EmployeeSSN` FOREIGN KEY (`Employee`) REFERENCES `EMPLOYEE` (`SSN`);

--
-- Constraints for table `EMPLOYEE`
--
ALTER TABLE `EMPLOYEE`
  ADD CONSTRAINT `FK_DepartmentNumber` FOREIGN KEY (`Department`) REFERENCES `DEPARTMENT` (`Number`),
  ADD CONSTRAINT `FK_Supervisor` FOREIGN KEY (`Supervisor`) REFERENCES `EMPLOYEE` (`SSN`);

--
-- Constraints for table `PROJECT`
--
ALTER TABLE `PROJECT`
  ADD CONSTRAINT `FK_DEPARTMENT` FOREIGN KEY (`Controlling_department`) REFERENCES `DEPARTMENT` (`Number`);

--
-- Constraints for table `WORKS_ON`
--
ALTER TABLE `WORKS_ON`
  ADD CONSTRAINT `FK_Project` FOREIGN KEY (`Project`) REFERENCES `PROJECT` (`Number`),
  ADD CONSTRAINT `FK_WORKS_ON` FOREIGN KEY (`SSN`) REFERENCES `EMPLOYEE` (`SSN`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
