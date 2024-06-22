-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2024 at 07:04 AM
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
  `booking_type` varchar(20) NOT NULL,
  `booking_date` datetime NOT NULL DEFAULT current_timestamp(),
  `status` int(11) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `asuransi_id` int(10) UNSIGNED DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `booking_airlines`
--

CREATE TABLE `booking_airlines` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `flight_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `booking_attractions`
--

CREATE TABLE `booking_attractions` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `attraction_provider_name` varchar(255) NOT NULL,
  `paket_attraction_id` int(10) UNSIGNED NOT NULL,
  `visit_date` date NOT NULL,
  `number_of_tickets` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `booking_hotels`
--

CREATE TABLE `booking_hotels` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `hotel_name` varchar(50) NOT NULL,
  `room_type` int(11) NOT NULL,
  `check_in_date` date NOT NULL,
  `check_out_date` date NOT NULL,
  `number_of_rooms` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `booking_rentals`
--

CREATE TABLE `booking_rentals` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `rental_provider_name` varchar(50) NOT NULL,
  `car_id` int(10) UNSIGNED NOT NULL,
  `pickup_date` datetime NOT NULL,
  `return_date` datetime NOT NULL,
  `pickup_location` varchar(255) NOT NULL,
  `return_location` varchar(255) NOT NULL,
  `is_with_driver` tinyint(1) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `migrations`
--

CREATE TABLE `migrations` (
  `id` int(10) UNSIGNED NOT NULL,
  `migration` varchar(255) NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(52, '2024_05_24_070034_create_flights_table', 1),
(81, '2024_05_24_071559_create_tickets_table', 2),
(101, '0001_01_01_000000_create_users_table', 3),
(102, '0001_01_01_000001_create_cache_table', 3),
(103, '2024_05_24_042216_airlines', 3),
(104, '2024_05_24_043821_hotels', 3),
(105, '2024_05_24_050634_create_personal_access_tokens_table', 3),
(106, '2024_05_24_051853_category', 3),
(107, '2024_05_24_061920_airline_class', 3),
(108, '2024_05_24_061958_airport', 3),
(109, '2025_05_24_042819_flight', 3),
(110, '2025_05_24_044345_tickets', 3),
(111, '2025_05_24_050924_rooms', 3),
(112, '2025_05_24_052259_bookings', 3),
(116, '2024_06_04_035543_create_bookings_table', 4),
(117, '2024_06_04_040459_create_booking__hotels_table', 4),
(118, '2024_06_04_044910_create_booking__airlines_table', 4),
(119, '2024_06_04_045026_create_booking__rentals_table', 4),
(120, '2024_06_04_045850_create_booking__attractions_table', 4);

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
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `booking_airlines`
--
ALTER TABLE `booking_airlines`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `booking_attractions`
--
ALTER TABLE `booking_attractions`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `booking_hotels`
--
ALTER TABLE `booking_hotels`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `booking_rentals`
--
ALTER TABLE `booking_rentals`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;

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

-- Table structure for table `reviews`
CREATE TABLE `reviews` (
  `id` int(10) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `rating` int(11) NOT NULL,
  `comment` text,
  `isEdited` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `reviews_booking_id_foreign` (`booking_id`),
  CONSTRAINT `reviews_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table creation for `review_rental`
CREATE TABLE `review_rental` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `review_id` int(10) UNSIGNED NOT NULL,
  `provider_name` varchar(100) NOT NULL,
  `category` enum('Car Cleanliness','Simple Pick-up And Drop-off Process','Staff is Helpful') NOT NULL,
  `count` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `review_rental_review_id_foreign` (`review_id`),
  CONSTRAINT `review_rental_review_id_foreign` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `review_hotel` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `review_id` int(10) UNSIGNED NOT NULL,
  `provider_name` varchar(100) NOT NULL,
  `category` enum('Strategic Location','Great Accomodation','Staff is Friendly') NOT NULL,
  `count` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `review_rental_review_id_foreign` (`review_id`),
  CONSTRAINT `review_rental_review_id_foreign` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `review_airline` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `review_id` int(10) UNSIGNED NOT NULL,
  `provider_name` varchar(100) NOT NULL,
  `category` enum('Car Cleanliness','Simple Pick-up And Drop-off Process','Staff is Helpful') NOT NULL,
  `count` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `review_rental_review_id_foreign` (`review_id`),
  CONSTRAINT `review_rental_review_id_foreign` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `review_attraction` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `review_id` int(10) UNSIGNED NOT NULL,
  `provider_name` varchar(100) NOT NULL,
  `category` enum('Car Cleanliness','Simple Pick-up And Drop-off Process','Staff is Helpful') NOT NULL,
  `count` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `review_rental_review_id_foreign` (`review_id`),
  CONSTRAINT `review_rental_review_id_foreign` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
-- Table structure for table `refund`
CREATE TABLE `refund` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `refund_ammount` decimal(10,2) NOT NULL,
  `refund_penalty` decimal(10,2) NOT NULL,
  `refund_reason` varchar(255) NOT NULL,
  `refund_status` varchar(255) NOT NULL DEFAULT 'pending',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `refund_booking_id_foreign` (`booking_id`),
  CONSTRAINT `refund_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

