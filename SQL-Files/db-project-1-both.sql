-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 06, 2018 at 01:49 AM
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
  `Dname` varchar(50) NOT NULL,
  `Dnumber` int(11) NOT NULL,
  `Manager_ssn` varchar(100) DEFAULT NULL,
  `Manager_start_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `DEPARTMENT`
--

INSERT INTO `DEPARTMENT` (`Dname`, `Dnumber`, `Manager_ssn`, `Manager_start_date`) VALUES
('Headquarters', 1, NULL, NULL),
('Networking', 3, NULL, NULL),
('Administration', 4, NULL, NULL),
('Research', 5, NULL, NULL),
('Software', 6, NULL, NULL),
('Hardware', 7, NULL, NULL),
('Sales', 8, NULL, NULL),
('HR', 9, NULL, NULL),
('QA', 11, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `DEPENDENT`
--

CREATE TABLE `DEPENDENT` (
  `Essn` varchar(15) NOT NULL,
  `Dependent_name` varchar(100) NOT NULL,
  `Sex` char(1) DEFAULT NULL,
  `Birth_date` date DEFAULT NULL,
  `Relationship` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `DEPENDENT`
--

INSERT INTO `DEPENDENT` (`Essn`, `Dependent_name`, `Sex`, `Birth_date`, `Relationship`) VALUES
('222222200', 'Jay Wallis', 'M', '1956-01-16', 'Spouse'),
('222222202', 'Amenda Vile', 'F', '1914-06-21', 'Children'),
('222222202', 'Mindy Vile', 'F', '1942-06-21', 'Spouse'),
('222222204', 'Amy Vos', 'F', '1963-11-11', 'Spouse'),
('222222204', 'james Vos', 'M', '1937-11-11', 'Children'),
('444444400', 'Kathy', 'F', '1944-10-09', 'Spouse'),
('444444401', 'Amy Bayes', 'F', '1926-06-18', 'Children'),
('444444401', 'Tom Bayes', 'M', '1926-06-20', 'Children'),
('444444401', 'William Bayes', 'M', '1954-06-19', 'Spouse'),
('666666601', 'Mary Jarvice', 'F', '1964-01-14', 'Spouse'),
('666666602', 'Bond King', 'M', '1964-04-16', 'Spouse'),
('666666604', 'Monia King', 'F', '1955-01-01', 'Spouse'),
('666666605', 'Aly Kramer', 'F', '1961-08-22', 'Spouse'),
('666666606', 'Chistina King', 'F', '1948-08-16', 'Spouse'),
('666666607', 'Alex Small', 'F', '1960-05-15', 'Spouse'),
('666666608', 'Katherin Head', 'F', '1964-05-19', 'Spouse'),
('666666608', 'Monica Head', 'F', '1937-05-19', 'Children'),
('666666608', 'Rachel Head', 'M', '1937-05-18', 'Children'),
('888665151', 'Mary Alice', 'F', '1924-11-10', 'Spouse'),
('987987987', 'Jalil Ahmad', 'M', '1929-03-29', 'Children'),
('987987987', 'Khadeja Begum', 'F', '1949-03-29', 'Spouse'),
('999887777', 'John Smith', 'M', '1956-07-19', 'Spouse');

-- --------------------------------------------------------

--
-- Table structure for table `DEPT_LOCATIONS`
--

CREATE TABLE `DEPT_LOCATIONS` (
  `Dnumber` int(11) NOT NULL,
  `Dlocation` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `DEPT_LOCATIONS`
--

INSERT INTO `DEPT_LOCATIONS` (`Dnumber`, `Dlocation`) VALUES
(1, 'Houston'),
(4, 'Stafford'),
(5, 'Bellaire'),
(5, 'Houston'),
(5, 'Sugarland'),
(6, 'Atlanta'),
(6, 'Sacramento'),
(7, 'Milwaukee'),
(8, 'Chicago'),
(8, 'Dallas'),
(8, 'Miami'),
(8, 'Philadephia'),
(8, 'Seattle'),
(9, 'Arlington'),
(11, 'Austin');

-- --------------------------------------------------------

--
-- Table structure for table `EMPLOYEE`
--

CREATE TABLE `EMPLOYEE` (
  `SSN` varchar(15) NOT NULL,
  `Fname` varchar(50) NOT NULL,
  `Minit` varchar(1) DEFAULT NULL,
  `Lname` varchar(50) NOT NULL,
  `Address` varchar(500) DEFAULT NULL,
  `Sex` varchar(6) DEFAULT NULL,
  `Birth_date` date DEFAULT NULL,
  `Salary` decimal(10,2) DEFAULT NULL,
  `Supervisor` varchar(15) DEFAULT NULL,
  `Department` int(11) NOT NULL,
  `Name` varchar(200)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `EMPLOYEE`
--

INSERT INTO `EMPLOYEE` (`SSN`, `Fname`, `Minit`, `Lname`, `Address`, `Sex`, `Birth_date`, `Salary`, `Supervisor`, `Department`, `Name`) VALUES
('001614905', 'Alex', 'C', 'Yu', '626 Mary St,Dallas,TX', 'M', '1980-10-17', '50000.00', '444444400', 6, 'Alex C Yu'),
('101248268', 'Lisa', 'G', 'House', '12 Maple St,Austin,TX', 'F', '1975-06-29', '85000.00', NULL, 7, 'Lisa G House'),
('110110110', 'Sunil', 'D', 'Gupta', '4312 Bowen Rd,Arlington,TX', 'M', '2001-02-01', '80000.00', '111111100', 3, 'Sunil D Gupta'),
('111111100', 'Jared', 'D', 'James', '123 Peachtr,Atlanta,GA', 'M', '1966-10-10', '85000.00', NULL, 6, 'Jared D James'),
('111111101', 'Jon', 'C', 'Jones', '111 Allgood,Atlanta,GA', 'M', '1967-11-14', '45000.00', '111111100', 6, 'Jon C Jones'),
('111111102', 'Justin', NULL, 'Mark', '2342 May,Atlanta,GA', 'M', '1966-01-12', '40000.00', '111111100', 6, 'Justin Mark'),
('111111103', 'Brad', 'C', 'Knight', '176 Main St.,Atlanta,GA', 'M', '1968-02-13', '44000.00', '111111100', 6, 'Brad C Knight'),
('111422203', 'Cameron', 'D', 'Thirteen', '22 Univ Blvd,Arlington,TX', 'F', '2001-05-04', '80000.00', '987987987', 4, 'Cameron D Thirteen'),
('112244668', 'Juan', 'G', 'Linda', '1210 Apple St,Austin,TX', 'F', '1965-06-23', '55000.00', NULL, 9, 'Juan G Linda'),
('123456789', 'John', 'B', 'Smith', '731 Fondren,Houston,TX', 'M', '1955-01-09', '30000.00', '333445555', 5, 'John B Smith'),
('202843824', 'Debra', 'T', 'Hall', '45 NY St,Rochester,NY', 'F', '1983-03-11', '30000.00', '555555501', 6, 'Debra T Hall'),
('214370999', 'Richard', 'T', 'Koelbel', '50 Elk St,Chicago,IL', 'M', '1976-04-03', '85000.00', '999999999', 4, 'Richard T Koelbel'),
('222222200', 'Evan', 'E', 'Wallis', '134 Pelham,Milwaukee,WI', 'M', '1958-01-16', '92000.00', NULL, 7, 'Evan E Wallis'),
('222222201', 'Josh', 'U', 'Zell', '266 McGrady,Milwaukee,WI', 'M', '1954-05-22', '56000.00', '222222200', 7, 'Josh U Zell'),
('222222202', 'Andy', 'C', 'Vile', '1967 Jordan,Milwaukee,WI', 'M', '1944-06-21', '53000.00', '222222200', 7, 'Andy C Vile'),
('222222203', 'Tom', 'G', 'Brand', '112 Third St,Milwaukee,WI', 'M', '1966-12-16', '62500.00', '222222200', 7, 'Tom G Brand'),
('222222204', 'Jenny', 'F', 'Vos', '263 Mayberry,Milwaukee,WI', 'F', '1967-11-11', '61000.00', '222222201', 7, 'Jenny F Vos'),
('222222205', 'Chris', 'A', 'Carter', '565 Jordan,Milwaukee,WI', 'F', '1960-03-21', '43000.00', '222222201', 7, 'Chris A Carter'),
('222333444', 'John', 'T', 'Ed', '4505 West St,Rochester,NY', 'M', '1981-02-18', '30000.00', '555555501', 6, 'John T Ed'),
('223344667', 'Jennifer', 'A', 'Joy', '1204 Main St,Miami,FL', 'F', '1976-05-19', '45000.00', '666666613', 8, 'Jennifer A Joy'),
('234234234', 'willie', 'D', 'Mary', '101 South St,Arlington,TX', 'F', '1961-12-20', '12000.00', '112244668', 9, 'willie D Mary'),
('241625699', 'Christina', 'S', 'Hisel', '37 Church Row,Rochester,NY', 'F', '1986-07-05', '45000.00', '123456789', 6, 'Christina S Hisel'),
('242535609', 'Erin', 'A', 'Maxfield', '123 Copper St,Arlington,TX', 'F', '1971-12-22', '72000.00', '555555500', 8, 'Erin A Maxfield'),
('242916639', 'Wilson', 'A', 'Holmes', '21 South Co,Arlington,TX', 'M', '1971-06-02', '72500.00', '555555500', 4, 'Wilson A Holmes'),
('245239264', 'Jake', 'D', 'Sheen', '20 North Co,Arlington,TX', 'M', '1954-12-25', '52000.00', '112244668', 6, 'Jake D Sheen'),
('254937381', 'Megan', 'G', 'Jones', '528 Stone CT,Chicago,IL', 'F', '1961-03-02', '62000.00', '666666600', 8, 'Megan G Jones'),
('292740167', 'Jisha', 'A', 'Carpenter', '194 Beachdr,Miami,FL', 'F', '1985-05-29', '15000.00', '666666613', 1, 'Jisha A Carpenter'),
('333333300', 'Kim', 'C', 'Grace', '667 Mills Ave,Sacramento,CA', 'F', '1970-10-23', '79000.00', NULL, 6, 'Kim C Grace'),
('333333301', 'Jeff', 'H', 'Chase', '15 Bradbury,Sacramento,CA', 'M', '1970-01-07', '44000.00', '333333300', 6, 'Jeff H Chase'),
('333445555', 'Frank', 'T', 'Wong', '638 Voss,Houston,TX', 'M', '1945-12-08', '40000.00', NULL, 5, 'Frank T Wong'),
('343434344', 'Jose', 'H', 'Barbara', '905 East St,Kleen,TX', 'F', '1955-02-28', '35000.00', '444444400', 6, 'Jose H Barbara'),
('349273344', 'Leonard', 'H', 'Moody', '908 Greek Row,Austin,TX', 'M', '1973-02-09', '45000.00', '444444400', 7, 'Leonard H Moody'),
('398172999', 'Percy', 'M', 'Liang', '14 Maple St,Austin,TX', 'M', '1991-06-12', '55000.00', NULL, 9, 'Percy M Liang'),
('432765098', 'Cindy', 'K', 'Burklow', '2015 Neil Ave,Miami,FL', 'F', '1984-02-23', '45000.00', '444444402', 6, 'Cindy K Burklow'),
('444212096', 'Gregory', 'G', 'Laurie', '78 Tree Cir,Houston,TX', 'M', '1969-09-15', '90000.00', '444444400', 7, 'Gregory G Laurie'),
('444222666', 'Kim', 'G', 'Ted', '3648 Tree Cir,Austin,TX', 'M', '1968-04-15', '50000.00', '999999999', 8, 'Kim G Ted'),
('444444400', 'Alex', 'D', 'Freed', '4333 Pillsbury,Milwaukee,WI', 'M', '1950-10-09', '89000.00', NULL, 7, 'Alex D Freed'),
('444444401', 'Bonnie', 'S', 'Bays', '111 Hollow,Milwaukee,WI', 'F', '1956-06-19', '70000.00', '444444400', 7, 'Bonnie S Bays'),
('444444402', 'Alec', 'C', 'Best', '233 Solid,Milwaukee,WI', 'M', '1966-06-18', '60000.00', '444444400', 7, 'Alec C Best'),
('444444403', 'Sam', 'S', 'Snedden', '97 Windy St,Milwaukee,WI', 'M', '1977-07-31', '48000.00', '444444400', 7, 'Sam S Snedden'),
('453453453', 'Joyce', 'A', 'English', '5631 Rice Oak,Houston,TX', 'F', '1962-07-31', '25000.00', '333445555', 5, 'Joyce A English'),
('555555500', 'John', 'C', 'James', '766 Bloomington,Sacramento,CA', 'M', '1975-06-30', '81000.00', NULL, 8, 'John C James'),
('555555501', 'Nandita', 'K', 'Ball', '222 Howard,Sacramento,CA', 'M', '1969-04-16', '62000.00', '555555500', 6, 'Nandita K Ball'),
('614370310', 'Andrea', 'M', 'Sondrini', '1450 Worthington St,Houston,TX', 'F', '1996-12-30', '65000.00', '444444401', 5, 'Andrea M Sondrini'),
('636669233', 'Michael', 'A', 'Morgan', '26 Sunset Blvd,Miami,FL', 'M', '1984-05-11', '73500.00', '666666612', 5, 'Michael A Morgan'),
('666666600', 'Bob', 'B', 'Bender', '8794 Garfield,Chicago,IL', 'M', '1968-04-17', '96000.00', NULL, 8, 'Bob B Bender'),
('666666601', 'Jill', 'J', 'Jarvis', '6234 Lincoln,Chicago,IL', 'F', '1966-01-14', '36000.00', '666666600', 8, 'Jill J Jarvis'),
('666666602', 'Kate', 'W', 'King', '1976 Boone Trace,Chicago,IL', 'F', '1966-04-16', '44000.00', '666666600', 8, 'Kate W King'),
('666666603', 'Lyle', 'G', 'Leslie', '417 Hancock Ave,Chicago,IL', 'M', '1963-06-09', '41000.00', '666666601', 8, 'Lyle G Leslie'),
('666666604', 'Billie', 'J', 'King', '556 Washington,Chicago,IL', 'F', '1960-01-01', '38000.00', '666666603', 8, 'Billie J King'),
('666666605', 'Jon', 'A', 'Kramer', '1988 Windy Creek,Seattle,WA', 'M', '1964-08-22', '41500.00', '666666603', 8, 'Jon A Kramer'),
('666666606', 'Ray', 'H', 'King', '213 Delk Road,Seattle,WA', 'M', '1949-08-16', '44500.00', '666666604', 8, 'Ray H King'),
('666666607', 'Gerald', 'D', 'Small', '122 Ball Street,Dallas,TX', 'M', '1962-05-15', '29000.00', '666666602', 8, 'Gerald D Small'),
('666666608', 'Arnold', 'A', 'Head', '233 Spring St,Dallas,TX', 'M', '1967-05-19', '33000.00', '666666602', 8, 'Arnold A Head'),
('666666609', 'Helga', 'C', 'Pataki', '101 Holyoke St,Dallas,TX', 'F', '1969-03-11', '32000.00', '666666602', 8, 'Helga C Pataki'),
('666666610', 'Naveen', 'B', 'Drew', '198 Elm St,Philadelphia,PA', 'M', '1970-05-23', '34000.00', '666666607', 8, 'Naveen B Drew'),
('666666611', 'Carl', 'E', 'Reedy', '213 Ball St,Philadelphia,PA', 'M', '1977-06-21', '32000.00', '666666610', 8, 'Carl E Reedy'),
('666666612', 'Sammy', 'G', 'Hall', '433 Main Street,Miami,FL', 'M', '1970-01-11', '37000.00', '666666611', 8, 'Sammy G Hall'),
('666666613', 'Red', 'A', 'Bacher', '196 Elm Street,Miami,FL', 'M', '1980-05-21', '33500.00', '666666612', 8, 'Red A Bacher'),
('666884444', 'Ramesh', 'K', 'Narayan', '971 Fire Oak,Humble,TX', 'M', '1952-09-15', '38000.00', '333445555', 5, 'Ramesh K Narayan'),
('673466642', 'Penny', 'G', 'Wolowitz', '42 South Blvd,Miami,FL', 'F', '1974-01-21', '17000.00', '222333444', 6, 'Penny G Wolowitz'),
('849934919', 'Sheldon', 'C', 'Cucuou', '11 Hollywood Blvd,Dallas,TX', 'M', '1974-03-22', '35500.00', NULL, 8, 'Sheldon C Cucuou'),
('888665151', 'James', 'E', 'Jordan', '450 Stone,Houston,TX', 'M', '1927-11-10', '55000.00', NULL, 1, 'James E Jordan'),
('906218888', 'James', 'U', 'Miller', '13 Fifth St,Seattle,WA', 'M', '1978-05-27', '75000.00', '999999999', 5, 'James U Miller'),
('913323708', 'Joseph', 'K', 'Kirkish', '22 UT Blvd,Austin,TX', 'M', '1996-03-04', '95000.00', NULL, 7, 'Joseph K Kirkish'),
('913353347', 'Zach', 'A', 'Geller', '333 PikeWay,Seattle,WA', 'M', '1990-08-15', '55000.00', '444444403', 6, 'Zach A Geller'),
('987654321', 'Jennifer', 'S', 'Wallace', '291 Berry,Bellaire,TX', 'F', '1931-06-20', '43000.00', NULL, 4, 'Jennifer S Wallace'),
('987987987', 'Ahmad', 'V', 'Jabbar', '980 Dallas,Houston,TX', 'M', '1959-03-29', '25000.00', '987654321', 4, 'Ahmad V Jabbar'),
('999887777', 'Alicia', 'J', 'Zelaya', '3321 Castle,Spring,TX', 'F', '1958-07-19', '25000.00', '987654321', 4, 'Alicia J Zelaya'),
('999999999', 'Roy', 'C', 'Lewallen', '14 Wynncrest Street,Dallas,TX', 'M', '1977-03-02', '75500.00', '666666600', 8, 'Roy C Lewallen');

-- --------------------------------------------------------

--
-- Table structure for table `PROJECT`
--

CREATE TABLE `PROJECT` (
  `Pname` varchar(50) NOT NULL,
  `Pnumber` int(11) NOT NULL,
  `Plocation` varchar(25) DEFAULT NULL,
  `Controlling_department` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `PROJECT`
--

INSERT INTO `PROJECT` (`Pname`, `Pnumber`, `Plocation`, `Controlling_department`) VALUES
('EntityAnnot', 4, 'Houston', 5),
('Analysis', 5, 'Sacramento', 6),
('EventManagement', 6, 'Sacramento', 6),
('FoodDistribution', 7, 'Sacramento', 6),
('Computerization', 10, 'Stafford', 4),
('ConfigMgmt', 11, 'Atlanta', 6),
('DataMining', 13, 'Sacramento', 6),
('Reorganization', 20, 'Houston', 1),
('SearchEngine', 22, 'Arlington', 6),
('MotherBoard', 29, 'Milwaukee', 7),
('Benefits', 30, 'Stafford', 4),
('OperatingSystem', 61, 'Sacramento', 6),
('DatabaseSystems', 62, 'Atlanta', 6),
('Middleware', 63, 'Atlanta', 6),
('Advertizing', 70, 'Arlington', 9),
('InkjetPrinters', 91, 'Milwaukee', 7),
('LaserPrinters', 92, 'Milwaukee', 7),
('HumanResource', 95, 'Arlington', 9);

-- --------------------------------------------------------

--
-- Table structure for table `WORKS_ON`
--

CREATE TABLE `WORKS_ON` (
  `Essn` varchar(15) NOT NULL,
  `Pno` int(11) NOT NULL,
  `Hours` decimal(3,1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `WORKS_ON`
--

INSERT INTO `WORKS_ON` (`Essn`, `Pno`, `Hours`) VALUES
('001614905', 13, '18.0'),
('101248268', 29, '10.0'),
('111111100', 61, '40.0'),
('111111101', 61, '40.0'),
('111111102', 61, '40.0'),
('111111103', 61, '40.0'),
('111422203', 4, '45.0'),
('111422203', 6, '5.0'),
('112244668', 95, '40.0'),
('123456789', 5, '32.5'),
('123456789', 6, '7.5'),
('202843824', 11, '20.0'),
('214370999', 5, '4.0'),
('214370999', 10, '35.0'),
('222222200', 62, '40.0'),
('222222201', 62, '48.0'),
('222222202', 62, '40.0'),
('222222203', 62, '40.0'),
('222222204', 62, '40.0'),
('222222205', 62, '40.0'),
('222333444', 91, '10.0'),
('223344667', 63, '20.0'),
('234234234', 95, '35.0'),
('241625699', 61, '4.0'),
('242535609', 62, '20.0'),
('242535609', 70, '20.0'),
('242916639', 4, '5.0'),
('242916639', 7, '10.0'),
('242916639', 11, '20.0'),
('245239264', 5, '5.0'),
('245239264', 10, '25.0'),
('245239264', 11, '25.0'),
('254937381', 70, '40.0'),
('292740167', 5, '25.0'),
('333333300', 63, '40.0'),
('333333301', 63, '46.0'),
('333445555', 7, '10.0'),
('333445555', 10, '10.0'),
('333445555', 20, '10.0'),
('343434344', 63, '40.0'),
('349273344', 6, '10.0'),
('349273344', 29, '15.0'),
('398172999', 7, '10.0'),
('398172999', 70, '10.0'),
('432765098', 63, '25.0'),
('444212096', 63, '25.0'),
('444222666', 62, '25.0'),
('444444400', 91, '40.0'),
('444444401', 91, '40.0'),
('444444402', 91, '40.0'),
('444444403', 91, '40.0'),
('453453453', 5, '20.0'),
('453453453', 6, '20.0'),
('555555500', 92, '40.0'),
('555555501', 92, '44.0'),
('636669233', 4, '11.0'),
('666666601', 91, '40.0'),
('666666603', 91, '40.0'),
('666666604', 91, '40.0'),
('666666605', 92, '40.0'),
('666666606', 91, '40.0'),
('666666607', 61, '40.0'),
('666666608', 62, '40.0'),
('666666609', 63, '40.0'),
('666666610', 61, '40.0'),
('666666611', 61, '40.0'),
('666666612', 61, '40.0'),
('666666613', 61, '30.0'),
('666666613', 62, '10.0'),
('666666613', 63, '10.0'),
('666884444', 7, '40.0'),
('673466642', 22, '4.0'),
('849934919', 95, '23.0'),
('906218888', 29, '15.0'),
('913323708', 92, '33.0'),
('913353347', 22, '30.0'),
('987654321', 20, '15.0'),
('987654321', 30, '20.0'),
('987987987', 10, '35.0'),
('987987987', 30, '5.0'),
('999887777', 10, '10.0'),
('999887777', 30, '30.0'),
('999999999', 5, '2.0'),
('999999999', 6, '2.0'),
('999999999', 7, '4.0'),
('999999999', 10, '4.0'),
('999999999', 20, '4.0'),
('999999999', 30, '4.0'),
('999999999', 61, '4.0'),
('999999999', 62, '4.0'),
('999999999', 63, '4.0'),
('999999999', 70, '2.0'),
('999999999', 91, '2.0'),
('999999999', 92, '1.0'),
('999999999', 95, '3.0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `DEPARTMENT`
--
ALTER TABLE `DEPARTMENT`
  ADD PRIMARY KEY (`Dnumber`),
  ADD UNIQUE KEY `Dname` (`Dname`),
  ADD KEY `Manager_ssn` (`Manager_ssn`);

--
-- Indexes for table `DEPENDENT`
--
ALTER TABLE `DEPENDENT`
  ADD PRIMARY KEY (`Essn`,`Dependent_name`);

--
-- Indexes for table `DEPT_LOCATIONS`
--
ALTER TABLE `DEPT_LOCATIONS`
  ADD PRIMARY KEY (`Dnumber`,`Dlocation`);

--
-- Indexes for table `EMPLOYEE`
--
ALTER TABLE `EMPLOYEE`
  ADD PRIMARY KEY (`SSN`),
  ADD KEY `Supervisor` (`Supervisor`),
  ADD KEY `Department` (`Department`);

--
-- Indexes for table `PROJECT`
--
ALTER TABLE `PROJECT`
  ADD PRIMARY KEY (`Pnumber`),
  ADD UNIQUE KEY `Pname` (`Pname`),
  ADD KEY `Controlling_department` (`Controlling_department`);

--
-- Indexes for table `WORKS_ON`
--
ALTER TABLE `WORKS_ON`
  ADD PRIMARY KEY (`Essn`,`Pno`),
  ADD KEY `Pno` (`Pno`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `DEPARTMENT`
--
ALTER TABLE `DEPARTMENT`
  ADD CONSTRAINT `DEPARTMENT_ibfk_1` FOREIGN KEY (`Manager_ssn`) REFERENCES `EMPLOYEE` (`SSN`);

--
-- Constraints for table `DEPT_LOCATIONS`
--
ALTER TABLE `DEPT_LOCATIONS`
  ADD CONSTRAINT `DEPT_LOCATIONS_ibfk_1` FOREIGN KEY (`Dnumber`) REFERENCES `DEPARTMENT` (`Dnumber`);

--
-- Constraints for table `EMPLOYEE`
--
ALTER TABLE `EMPLOYEE`
  ADD CONSTRAINT `EMPLOYEE_ibfk_1` FOREIGN KEY (`Supervisor`) REFERENCES `EMPLOYEE` (`SSN`),
  ADD CONSTRAINT `EMPLOYEE_ibfk_2` FOREIGN KEY (`Department`) REFERENCES `DEPARTMENT` (`Dnumber`);

--
-- Constraints for table `PROJECT`
--
ALTER TABLE `PROJECT`
  ADD CONSTRAINT `PROJECT_ibfk_1` FOREIGN KEY (`Controlling_department`) REFERENCES `DEPARTMENT` (`Dnumber`);

--
-- Constraints for table `WORKS_ON`
--
ALTER TABLE `WORKS_ON`
  ADD CONSTRAINT `WORKS_ON_ibfk_1` FOREIGN KEY (`Essn`) REFERENCES `EMPLOYEE` (`SSN`),
  ADD CONSTRAINT `WORKS_ON_ibfk_2` FOREIGN KEY (`Pno`) REFERENCES `PROJECT` (`Pnumber`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
