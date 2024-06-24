CREATE TABLE IF NOT EXISTS `bookings` (
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

CREATE TABLE IF NOT EXISTS `booking_airlines` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `flight_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `booking_attractions` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `attraction_provider_name` varchar(255) NOT NULL,
  `paket_attraction_id` int(10) UNSIGNED NOT NULL,
  `visit_date` date NOT NULL,
  `number_of_tickets` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `booking_hotels` (
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

CREATE TABLE IF NOT EXISTS `booking_rentals` (
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

CREATE TABLE IF NOT EXISTS `reviews` (
  `id` int(10) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `rating` int(11) NOT NULL,
  `comment` text,
  `isEdited` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  -- KEY `reviews_booking_id_foreign` (`booking_id`),
  -- CONSTRAINT `reviews_booking_id_foreign` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- CREATE TABLE IF NOT EXISTS `review_rental` (
--   `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
--   `review_id` int(10) UNSIGNED NOT NULL,
--   `provider_name` varchar(100) NOT NULL,
--   `category` enum('Car Cleanliness','Simple Pick-up And Drop-off Process','Staff is Helpful') NOT NULL,
--   `count` int(11) NOT NULL,
--   `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
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
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
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
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
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
--   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
--   PRIMARY KEY (`id`),
--   KEY `review_attraction_review_id_foreign` (`review_id`),
--   CONSTRAINT `fk_review_attraction_review_id` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`) ON DELETE CASCADE
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;