-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 06, 2019 at 03:39 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `thesis_project_ucc`
--

-- --------------------------------------------------------

--
-- Table structure for table `pharmacy`
--

CREATE TABLE `pharmacy` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `address` text NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pharmacy`
--

INSERT INTO `pharmacy` (`id`, `name`, `address`, `latitude`, `longitude`) VALUES
(1, 'Irwins Midnight Pharmacy Shandon', '77 Shandon St, Gurranabraher, Cork, T23 HP74', 51.902335, -8.4809947),
(2, 'Phelan\'s Late Night Pharmacy', '9 St Patrick\'s St, Centre, Cork, T12 X79F', 51.899715, -8.4726667),
(3, 'College Road Pharmacy', '61 College Rd, Glasheen, Cork, T12 X5F3', 51.8918134, -8.4963111),
(4, 'Brodericks Chemist', '84 Barrack St, The Lough, Greenmount, Co. Cork', 51.892801, -8.4827757),
(5, 'Dennehy\'s cross pharmacy', 'Wilton Rd, Glasheen, Cork', 51.8888061, -8.5088553),
(6, 'Daltons Pharmacy', 'Unit 11, N Main St, Centre, Cork, T12 E77Y', 51.9003245, -8.4810175),
(7, 'Allcare Late Night Pharmacy Wilton', '4 Cardinal way, Wilton, Cork, T12 VY9X', 51.8813754, -8.5125065),
(8, 'Horgan\'s Pharmacy', 'South Gate Bridge, Barrack St, Cork', 51.8951555, -8.4782723),
(9, 'O\'Donovan\'s Life Pharmacy Ballyphehane', '4 Pearse Square, Ballyphehane, Cork', 51.8834262, -8.4848241),
(10, 'Santrys Washington Street Pharmacy', '25A Washington Street West, Centre, Cork', 51.8975572, -8.4823063),
(11, 'O\'Sullivans Pharmacy Douglas', 'South Douglas Road, Cork', 51.8793592, -8.4473164),
(12, 'Johnson\'s Pharmacy', 'Victoria Cross, Cork', 51.8929865, -8.5070397),
(13, 'Lloyds Pharmacy', 'Glenastar, 42 Togher Rd, Togher, Cork, T12 RY10', 51.8929852, -8.5223606),
(14, 'Minihan\'s Pharmacy', '108 Oliver Plunkett St, Centre, Cork', 51.8979993, -8.4729075),
(15, 'Dan McCarthys Pharmacy', 'St Patrick\'s St, Centre, Cork, T12 K5FK', 51.8985239, -8.4751338);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pharmacy`
--
ALTER TABLE `pharmacy`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
