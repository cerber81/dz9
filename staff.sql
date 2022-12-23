-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 23, 2022 at 04:24 PM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sem9`
--

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `id` int(12) UNSIGNED NOT NULL,
  `date_added` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `adopted` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `surname` varchar(30) DEFAULT '-----',
  `name` varchar(30) DEFAULT '-----',
  `firs_name` varchar(30) DEFAULT '-----',
  `years` int(2) DEFAULT NULL,
  `city` varchar(50) DEFAULT '-----',
  `post` varchar(100) DEFAULT '-----',
  `salary` int(6) DEFAULT NULL,
  `user_id` varchar(20) NOT NULL,
  `telegram` varchar(30) NOT NULL DEFAULT '-----',
  `resume` text,
  `portfolio` text,
  `status` int(1) DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`id`, `date_added`, `adopted`, `surname`, `name`, `firs_name`, `years`, `city`, `post`, `salary`, `user_id`, `telegram`, `resume`, `portfolio`, `status`) VALUES
(5, '2022-12-20 17:18:45', '2022-12-23 17:27:48', 'Иванов', 'Иван', 'Иванович', 32, 'Москва', 'менеджер', 30000, '44525252', 'ivanov', 'https://sity1.ru', 'https://sity2.ru', 2),
(6, '2022-12-21 13:59:40', '2022-12-22 13:59:40', 'Петров', 'Петр', 'Петрович', 30, 'Ростов', 'Проджект', 36000, '45452525', 'prteov', 'https://sity1.ru', 'https://sity2.ru', 2),
(7, '2022-12-23 17:32:09', '2022-12-23 17:32:09', 'Игнатова', 'Марина', '-----', 28, 'Волгоград', 'дизайнер', 50000, '4875956', 'ignatova', 'https://sity1', 'https://sity2', 1),
(8, '2022-12-23 17:36:44', '2022-12-23 17:36:44', 'Андрющенко', 'Ирина', 'Михайловна', 33, 'Волгоград', 'дизайнер', 55000, '4875956', 'andri', 'https://sity1.ru', 'https://sity2.ru', 1),
(9, '2022-12-23 17:40:29', '2022-12-23 17:40:29', 'Карташова', 'Маргарита', 'Сергеевна', 21, 'Москва', 'дизайнер', 30000, '937933861', 'kart', 'https://sity1', 'https://sity2.ru', 1),
(10, '2022-12-23 17:45:34', '2022-12-23 18:19:25', 'Ларионова', 'Наталья', 'Ивановна', 28, 'Москва', 'учитель', 35000, '937933861', 'larion', 'https://sity1.ru', 'https://sity2.ru', 2),
(11, '2022-12-23 17:47:23', '2022-12-23 18:18:17', 'Рудакова', 'Екатерина', 'Вячеславовна', 42, 'Москва', 'учитель', 35000, '937933861', 'rydakova', 'https://sity1.ru', 'https://sity2.ru', 2),
(12, '2022-12-23 18:14:29', '2022-12-23 18:14:29', 'Борщев', 'Вячеслав', 'Павлович', 50, 'Саратов', 'Инженер', 70000, '937933861', 'borsh', 'https://sity1.ru', 'https://sity2.ru', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `id` int(12) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
