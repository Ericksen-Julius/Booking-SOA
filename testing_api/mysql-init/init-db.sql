-- CREATE TABLE IF NOT EXISTS `bookings` (
--   `id` int(10) UNSIGNED NOT NULL,
--   `user_id` int(10) UNSIGNED NOT NULL,
--   `booking_type` varchar(20) NOT NULL,
--   `booking_date` datetime NOT NULL DEFAULT current_timestamp(),
--   `status` int(11) NOT NULL,
--   `total_price` decimal(10,2) NOT NULL,
--   `asuransi_id` int(10) UNSIGNED DEFAULT NULL,
--   `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
--   `updated_at` timestamp NULL DEFAULT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- CREATE TABLE IF NOT EXISTS `booking_airlines` (
--   `id` bigint(20) UNSIGNED NOT NULL,
--   `booking_id` int(10) UNSIGNED NOT NULL,
--   `flight_id` int(11) NOT NULL,
--   `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- CREATE TABLE IF NOT EXISTS `booking_attractions` (
--   `id` bigint(20) UNSIGNED NOT NULL,
--   `booking_id` int(10) UNSIGNED NOT NULL,
--   `attraction_provider_name` varchar(255) NOT NULL,
--   `paket_attraction_id` int(10) UNSIGNED NOT NULL,
--   `visit_date` date NOT NULL,
--   `number_of_tickets` int(11) NOT NULL,
--   `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- CREATE TABLE IF NOT EXISTS `booking_hotels` (
--   `id` bigint(20) UNSIGNED NOT NULL,
--   `booking_id` int(10) UNSIGNED NOT NULL,
--   `hotel_name` varchar(50) NOT NULL,
--   `room_type` int(11) NOT NULL,
--   `check_in_date` date NOT NULL,
--   `check_out_date` date NOT NULL,
--   `number_of_rooms` int(11) NOT NULL,
--   `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- CREATE TABLE IF NOT EXISTS `booking_rentals` (
--   `id` bigint(20) UNSIGNED NOT NULL,
--   `booking_id` int(10) UNSIGNED NOT NULL,
--   `rental_provider_name` varchar(50) NOT NULL,
--   `car_id` int(10) UNSIGNED NOT NULL,
--   `pickup_date` datetime NOT NULL,
--   `return_date` datetime NOT NULL,
--   `pickup_location` varchar(255) NOT NULL,
--   `return_location` varchar(255) NOT NULL,
--   `is_with_driver` tinyint(1) NOT NULL,
--   `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- CREATE TABLE IF NOT EXISTS `reviews` (
--   `id` int(10) UNSIGNED NOT NULL,
--   `booking_id` int(10) UNSIGNED NOT NULL,
--   `rating` int(11) NOT NULL,
--   `comment` text,
--   `isEdited` tinyint(1) NOT NULL DEFAULT 0,
--   `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
--   PRIMARY KEY (`id`),
--   KEY `reviews_booking_id_foreign` (`booking_id`),
--   CONSTRAINT `reviews_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- CREATE TABLE IF NOT EXISTS `review_rental` (
--   `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
--   `review_id` int(10) UNSIGNED NOT NULL,
--   `provider_name` varchar(100) NOT NULL,
--   `category` enum('Car Cleanliness','Simple Pick-up And Drop-off Process','Staff is Helpful') NOT NULL,
--   `count` int(11) NOT NULL,
--   `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
--   PRIMARY KEY (`id`),
--   KEY `review_rental_review_id_foreign` (`review_id`),
--   CONSTRAINT `fk_review_rental_review_id` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`) ON DELETE CASCADE
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- CREATE TABLE IF NOT EXISTS `review_hotel` (
--   `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
--   `review_id` int(10) UNSIGNED NOT NULL,
--   `provider_name` varchar(100) NOT NULL,
--   `category` enum('Strategic Location','Great Accomodation','Staff is Friendly') NOT NULL,
--   `count` int(11) NOT NULL,
--   `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
--   PRIMARY KEY (`id`),
--   KEY `review_hotel_review_id_foreign` (`review_id`),
--   CONSTRAINT `fk_review_hotel_review_id` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`) ON DELETE CASCADE
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- CREATE TABLE IF NOT EXISTS `review_airline` (
--   `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
--   `review_id` int(10) UNSIGNED NOT NULL,
--   `provider_name` varchar(100) NOT NULL,
--   `category` enum('Punctuality','Cabin Crew Service','Seat Comfort') NOT NULL,
--   `count` int(11) NOT NULL,
--   `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
--   PRIMARY KEY (`id`),
--   KEY `review_airline_review_id_foreign` (`review_id`),
--   CONSTRAINT `fk_review_airline_review_id` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`) ON DELETE CASCADE
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- CREATE TABLE IF NOT EXISTS `review_attraction` (
--   `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
--   `review_id` int(10) UNSIGNED NOT NULL,
--   `provider_name` varchar(100) NOT NULL,
--   `category` enum('Visitor Experience','Facilities','Staff Friendliness') NOT NULL,
--   `count` int(11) NOT NULL,
--   `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
--   PRIMARY KEY (`id`),
--   KEY `review_attraction_review_id_foreign` (`review_id`),
--   CONSTRAINT `fk_review_attraction_review_id` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`) ON DELETE CASCADE
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 24, 2024 at 01:29 PM
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


-- --------------------------------------------------------

--
-- Table structure for table `refund`
--

CREATE TABLE `refund` (
  `id` int(10) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `refund_ammount` decimal(10,2) NOT NULL,
  `refund_penalty` decimal(10,2) NOT NULL,
  `refund_reason` varchar(255) NOT NULL,
  `refund_status` varchar(255) NOT NULL DEFAULT 'pending',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reviews`
--

CREATE TABLE `reviews` (
  `id` int(10) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `rating` int(11) NOT NULL,
  `comment` text DEFAULT NULL,
  `isEdited` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

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
-- Indexes for table `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `refund`
--
ALTER TABLE `refund`
  ADD PRIMARY KEY (`id`),
  ADD KEY `refund_booking_id_foreign` (`booking_id`);

--
-- Indexes for table `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`id`),
  ADD KEY `reviews_booking_id_foreign` (`booking_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

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
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `booking_rentals`
--
ALTER TABLE `booking_rentals`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;

--
-- AUTO_INCREMENT for table `refund`
--
ALTER TABLE `refund`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

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
-- Constraints for table `refund`
--
ALTER TABLE `refund`
  ADD CONSTRAINT `refund_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `reviews_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
