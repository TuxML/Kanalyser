-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 30, 2018 at 07:34 PM
-- Server version: 5.7.22-0ubuntu0.16.04.1
-- PHP Version: 7.0.28-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `IrmaDB_prod`
--

-- --------------------------------------------------------

--
-- Table structure for table `Compilations`
--

CREATE TABLE `Compilations` (
  `cid` int(11) NOT NULL,
  `compilation_date` datetime NOT NULL,
  `compilation_time` float NOT NULL,
  `config_file` longblob NOT NULL,
  `stdlog_file` longblob NOT NULL,
  `errlog_file` longblob NOT NULL,
  `output_file` longblob,
  `core_size` int(11) NOT NULL,
  `dependencies` longtext NOT NULL,
  `gcc_version` varchar(32) NOT NULL,
  `libc_version` varchar(32) NOT NULL,
  `core_used` int(11) NOT NULL,
  `incremental_mod` tinyint(1) NOT NULL,
  `tuxml_version` varchar(32) NOT NULL,
  `git_branch` varchar(32) NOT NULL,
  `docker_image` varchar(32) NOT NULL,
  `os` varchar(32) NOT NULL,
  `distribution` varchar(32) NOT NULL,
  `distrib_version` varchar(32) NOT NULL,
  `kernel` varchar(32) NOT NULL,
  `arch` varchar(32) NOT NULL,
  `cpu` varchar(128) NOT NULL,
  `cpu_cores` int(11) NOT NULL,
  `cpu_freq` varchar(32) NOT NULL,
  `ram` int(11) NOT NULL,
  `mechanical_drive` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Incremental_compilations`
--

CREATE TABLE `Incremental_compilations` (
  `cid_incmod` int(11) NOT NULL,
  `cid_origin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Properties`
--

CREATE TABLE `Properties` (
  `id` int(11) NOT NULL,
  `name` varchar(256) NOT NULL,
  `type` enum('BOOL','HEX','INT','STRING','TRISTATE','UNKNOWN') NOT NULL DEFAULT 'UNKNOWN'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Tests`
--

CREATE TABLE `Tests` (
  `tid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `test_date` datetime NOT NULL,
  `boot_time` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Compilations`
--
ALTER TABLE `Compilations`
  ADD PRIMARY KEY (`cid`),
  ADD UNIQUE KEY `cid` (`cid`);

--
-- Indexes for table `Incremental_compilations`
--
ALTER TABLE `Incremental_compilations`
  ADD PRIMARY KEY (`cid_incmod`,`cid_origin`),
  ADD KEY `cid_origin` (`cid_origin`);

--
-- Indexes for table `Properties`
--
ALTER TABLE `Properties`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Tests`
--
ALTER TABLE `Tests`
  ADD PRIMARY KEY (`tid`),
  ADD UNIQUE KEY `tid` (`tid`),
  ADD KEY `cid` (`cid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Compilations`
--
ALTER TABLE `Compilations`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3214;
--
-- AUTO_INCREMENT for table `Properties`
--
ALTER TABLE `Properties`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12798;
--
-- AUTO_INCREMENT for table `Tests`
--
ALTER TABLE `Tests`
  MODIFY `tid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3214;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `Incremental_compilations`
--
ALTER TABLE `Incremental_compilations`
  ADD CONSTRAINT `Incremental_compilations_ibfk_1` FOREIGN KEY (`cid_incmod`) REFERENCES `Compilations` (`cid`),
  ADD CONSTRAINT `Incremental_compilations_ibfk_2` FOREIGN KEY (`cid_origin`) REFERENCES `Compilations` (`cid`);

--
-- Constraints for table `Tests`
--
ALTER TABLE `Tests`
  ADD CONSTRAINT `Tests_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `Compilations` (`cid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
