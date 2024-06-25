-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2024 at 10:53 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `microservices_soa_h`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `id` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `booking_code` varchar(10) NOT NULL,
  `booking_type` varchar(20) NOT NULL,
  `booking_date` datetime NOT NULL DEFAULT current_timestamp(),
  `provider_name` varchar(100) NOT NULL,
  `status` int(11) NOT NULL DEFAULT 0,
  `total_price` decimal(10,2) NOT NULL,
  `asuransi_id` int(10) UNSIGNED DEFAULT NULL,
  `service_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`id`, `user_id`, `booking_code`, `booking_type`, `booking_date`, `provider_name`, `status`, `total_price`, `asuransi_id`, `service_id`, `created_at`, `updated_at`) VALUES
(22, 1, 'HTYV53', 'Hotel', '2024-06-10 09:51:44', 'Amaris', 1, 200000.00, NULL, 0, '2024-06-10 02:51:44', NULL),
(23, 1, 'AWPC35', 'Airline', '2024-06-10 09:53:55', 'Garuda', 0, 200000.00, 1, 0, '2024-06-10 02:53:55', NULL),
(24, 1, 'RUGN79', 'Rental', '2024-06-10 09:54:18', 'Bro', 0, 150000.00, NULL, 0, '2024-06-10 02:54:18', NULL),
(50, 1, 'TGBL56', 'Attraction', '2024-06-15 16:24:27', 'Jatim Park', 0, 75000.00, NULL, 0, '2024-06-15 09:24:27', NULL),
(55, 1, 'HMZM00', 'Hotel', '2024-06-25 12:36:19', 'Merlyn Hotel', 0, 700000.00, NULL, 1, '2024-06-25 05:36:19', NULL),
(56, 2, 'HPQF82', 'Hotel', '2024-06-25 12:36:50', 'Merlyn Hotel', 0, 900000.00, NULL, 2, '2024-06-25 05:36:50', NULL),
(57, 3, 'HTOE71', 'Hotel', '2024-06-25 12:37:09', 'Merlyn Hotel', 0, 400000.00, NULL, 2, '2024-06-25 05:37:09', NULL),
(59, 3, 'HNFE12', 'Hotel', '2024-06-25 12:37:59', 'Amaris', 0, 400000.00, NULL, 2, '2024-06-25 05:37:59', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `booking_airlines`
--

CREATE TABLE `booking_airlines` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `flight_id` varchar(10) NOT NULL,
  `flight_date` date NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `booking_airlines`
--

INSERT INTO `booking_airlines` (`id`, `booking_id`, `flight_id`, `flight_date`, `created_at`, `updated_at`) VALUES
(2, 23, 'C302', '2024-08-04', '2024-06-10 02:53:55', '2024-06-15 09:18:44');

-- --------------------------------------------------------

--
-- Table structure for table `booking_attractions`
--

CREATE TABLE `booking_attractions` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `paket_attraction_id` int(10) UNSIGNED NOT NULL,
  `visit_date` date NOT NULL,
  `number_of_tickets` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `booking_attractions`
--

INSERT INTO `booking_attractions` (`id`, `booking_id`, `paket_attraction_id`, `visit_date`, `number_of_tickets`, `created_at`, `updated_at`) VALUES
(3, 50, 1, '2024-07-04', 3, '2024-06-15 09:24:27', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `booking_hotels`
--

CREATE TABLE `booking_hotels` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `room_type` int(11) NOT NULL,
  `check_in_date` date NOT NULL,
  `check_out_date` date NOT NULL,
  `number_of_rooms` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `booking_hotels`
--

INSERT INTO `booking_hotels` (`id`, `booking_id`, `room_type`, `check_in_date`, `check_out_date`, `number_of_rooms`, `created_at`, `updated_at`) VALUES
(10, 22, 1, '2024-07-04', '2024-08-04', 2, '2024-06-10 02:51:44', NULL),
(34, 55, 2, '2024-06-26', '2024-06-28', 2, '2024-06-25 05:36:19', NULL),
(35, 56, 1, '2024-06-26', '2024-06-29', 1, '2024-06-25 05:36:50', NULL),
(36, 57, 1, '2024-06-26', '2024-06-29', 2, '2024-06-25 05:37:09', NULL),
(38, 59, 2, '2024-06-27', '2024-06-29', 2, '2024-06-25 05:37:59', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `booking_rentals`
--

CREATE TABLE `booking_rentals` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `car_id` int(10) UNSIGNED NOT NULL,
  `pickup_date` datetime NOT NULL,
  `return_date` datetime NOT NULL,
  `pickup_location` varchar(255) NOT NULL,
  `return_location` varchar(255) NOT NULL,
  `is_with_driver` tinyint(1) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `booking_rentals`
--

INSERT INTO `booking_rentals` (`id`, `booking_id`, `car_id`, `pickup_date`, `return_date`, `pickup_location`, `return_location`, `is_with_driver`, `created_at`, `updated_at`) VALUES
(2, 24, 1, '2024-07-04 00:00:00', '2024-08-04 00:00:00', 'Siwalankerto', 'Petra Gedung Q', 1, '2024-06-10 02:54:18', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `reviews`
--

CREATE TABLE `reviews` (
  `id` int(10) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `rating` int(1) NOT NULL,
  `comment` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `reviews`
--

INSERT INTO `reviews` (`id`, `booking_id`, `rating`, `comment`, `created_at`, `updated_at`) VALUES
(7, 22, 4, 'Enak sekali', '2024-06-25 05:29:49', NULL),
(8, 55, 5, 'Enak sekali', '2024-06-25 05:45:36', NULL),
(9, 56, 4, 'Enak sekali', '2024-06-25 05:46:04', NULL),
(10, 57, 3, 'Enak sekali', '2024-06-25 05:46:22', NULL),
(11, 59, 5, 'Enak sekali', '2024-06-25 05:46:33', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `review_options`
--

CREATE TABLE `review_options` (
  `id` int(10) UNSIGNED NOT NULL,
  `rating_group` enum('1-2','3-4','5') NOT NULL,
  `provider_type` enum('Airline','Hotel','Rental','Attraction') NOT NULL,
  `option_text` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `review_options`
--

INSERT INTO `review_options` (`id`, `rating_group`, `provider_type`, `option_text`) VALUES
(1, '1-2', 'Hotel', 'Poor customer service'),
(2, '1-2', 'Hotel', 'Room was dirty'),
(3, '1-2', 'Hotel', 'Noisy environment'),
(4, '1-2', 'Hotel', 'Uncomfortable bed'),
(5, '1-2', 'Hotel', 'Facilities not as advertised'),
(6, '3-4', 'Hotel', 'Could be cleaner'),
(7, '3-4', 'Hotel', 'Staff could be more helpful'),
(8, '3-4', 'Hotel', 'Limited breakfast options'),
(9, '3-4', 'Hotel', 'Average room amenities'),
(10, '5', 'Hotel', 'Excellent service'),
(11, '5', 'Hotel', 'Very clean'),
(12, '5', 'Hotel', 'Comfortable bed'),
(13, '5', 'Hotel', 'Great location'),
(14, '5', 'Hotel', 'Friendly staff'),
(15, '1-2', 'Airline', 'Poor customer service'),
(16, '1-2', 'Airline', 'Flight was delayed'),
(17, '1-2', 'Airline', 'Lost luggage'),
(18, '1-2', 'Airline', 'Uncomfortable seating'),
(19, '1-2', 'Airline', 'Inadequate in-flight entertainment'),
(20, '3-4', 'Airline', 'Could be cleaner'),
(21, '3-4', 'Airline', 'Staff could be more attentive'),
(22, '3-4', 'Airline', 'Limited food options'),
(23, '3-4', 'Airline', 'Average legroom'),
(24, '5', 'Airline', 'Excellent service'),
(25, '5', 'Airline', 'Comfortable seating'),
(26, '5', 'Airline', 'On-time flight'),
(27, '5', 'Airline', 'Great in-flight entertainment'),
(28, '5', 'Airline', 'Friendly staff'),
(29, '1-2', 'Rental', 'Poor customer service'),
(30, '1-2', 'Rental', 'Car was dirty'),
(31, '1-2', 'Rental', 'Long wait time'),
(32, '1-2', 'Rental', 'Hidden fees'),
(33, '1-2', 'Rental', 'Unreliable vehicle'),
(34, '3-4', 'Rental', 'Could be cleaner'),
(35, '3-4', 'Rental', 'Staff could be more helpful'),
(36, '3-4', 'Rental', 'Limited vehicle options'),
(37, '3-4', 'Rental', 'Average rental price'),
(38, '5', 'Rental', 'Excellent service'),
(39, '5', 'Rental', 'Clean car'),
(40, '5', 'Rental', 'Quick and easy process'),
(41, '5', 'Rental', 'Fair pricing'),
(42, '5', 'Rental', 'Friendly staff'),
(43, '1-2', 'Attraction', 'Poor customer service'),
(44, '1-2', 'Attraction', 'Attraction was dirty'),
(45, '1-2', 'Attraction', 'Overcrowded'),
(46, '1-2', 'Attraction', 'Long wait times'),
(47, '1-2', 'Attraction', 'Unclear instructions/signage'),
(48, '3-4', 'Attraction', 'Could be cleaner'),
(49, '3-4', 'Attraction', 'Staff could be more helpful'),
(50, '3-4', 'Attraction', 'Limited facilities'),
(51, '3-4', 'Attraction', 'Average value for money'),
(52, '5', 'Attraction', 'Excellent service'),
(53, '5', 'Attraction', 'Very clean'),
(54, '5', 'Attraction', 'Well-organized'),
(55, '5', 'Attraction', 'Great value for money'),
(56, '5', 'Attraction', 'Friendly staff');

-- --------------------------------------------------------

--
-- Table structure for table `review_selections`
--

CREATE TABLE `review_selections` (
  `id` int(10) UNSIGNED NOT NULL,
  `review_id` int(10) UNSIGNED NOT NULL,
  `option_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `review_selections`
--

INSERT INTO `review_selections` (`id`, `review_id`, `option_id`) VALUES
(1, 7, 10),
(2, 7, 11),
(3, 7, 12),
(4, 8, 10),
(5, 8, 11),
(6, 8, 12),
(7, 9, 6),
(8, 9, 7),
(9, 10, 8),
(10, 10, 9);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `booking_airlines`
--
ALTER TABLE `booking_airlines`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_airlines_booking_id_foreign` (`booking_id`);

--
-- Indexes for table `booking_attractions`
--
ALTER TABLE `booking_attractions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_attractions_booking_id_foreign` (`booking_id`);

--
-- Indexes for table `booking_hotels`
--
ALTER TABLE `booking_hotels`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_hotels_booking_id_foreign` (`booking_id`);

--
-- Indexes for table `booking_rentals`
--
ALTER TABLE `booking_rentals`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_rentals_booking_id_foreign` (`booking_id`);

--
-- Indexes for table `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking_id` (`booking_id`);

--
-- Indexes for table `review_options`
--
ALTER TABLE `review_options`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `review_selections`
--
ALTER TABLE `review_selections`
  ADD PRIMARY KEY (`id`),
  ADD KEY `review_id` (`review_id`),
  ADD KEY `option_id` (`option_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT for table `booking_airlines`
--
ALTER TABLE `booking_airlines`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `booking_attractions`
--
ALTER TABLE `booking_attractions`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `booking_hotels`
--
ALTER TABLE `booking_hotels`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `booking_rentals`
--
ALTER TABLE `booking_rentals`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `reviews`
--
ALTER TABLE `reviews`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `review_options`
--
ALTER TABLE `review_options`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `review_selections`
--
ALTER TABLE `review_selections`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking_airlines`
--
ALTER TABLE `booking_airlines`
  ADD CONSTRAINT `booking_airlines_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `booking_attractions`
--
ALTER TABLE `booking_attractions`
  ADD CONSTRAINT `booking_attractions_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `booking_hotels`
--
ALTER TABLE `booking_hotels`
  ADD CONSTRAINT `booking_hotels_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `booking_rentals`
--
ALTER TABLE `booking_rentals`
  ADD CONSTRAINT `booking_rentals_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `review_selections`
--
ALTER TABLE `review_selections`
  ADD CONSTRAINT `review_selections_ibfk_1` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `review_selections_ibfk_2` FOREIGN KEY (`option_id`) REFERENCES `review_options` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
