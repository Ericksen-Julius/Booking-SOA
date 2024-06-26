from nameko.extensions import DependencyProvider
import json

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
import random
import string
# from statistics import mean


def generate_string():
    letters_part = ''.join(random.choices(string.ascii_uppercase, k=3))
    digits_part = ''.join(random.choices(string.digits, k=2))
    return letters_part + digits_part

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection
    
# Review related methods
        # Review related methods
    def add_review(self, booking_id, rating, comment, option_ids):
        try:
            cursor = self.connection.cursor(dictionary=True)
            if not self.check_booking_exists(booking_id):
                return {'error': 'Booking does not exist', 'status': 404}
            sql = "INSERT INTO reviews (`booking_id`, `rating`, `comment`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (booking_id, rating, comment))
            self.connection.commit()
            inserted_id = cursor.lastrowid
            cursor.close()
            check = self.add_review_selection(option_ids=option_ids, inserted_id=inserted_id)
            if check['success']:
                return {'message': 'Review added successfully', 'status': 200}
            else:
                return {'error': 'Failed to add review selections', 'status': 500}
        except Exception as e:
            return {'error': str(e), 'status': 500}
        
    def get_rating_type(self, service_type):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = """
                    SELECT a.provider_name, ROUND(AVG(b.rating), 2) AS average_rating
                    FROM bookings AS a
                    JOIN reviews AS b ON a.id = b.booking_id
                    WHERE LOWER(a.booking_type) = %s
                    GROUP BY a.provider_name;
                """
            cursor.execute(sql, (service_type,))
            results = cursor.fetchall()
            cursor.close()
            for result in results:
                result['average_rating'] = float(result['average_rating'])

            if not results:
                return {'error': 'No data found', 'status': 404}
            return {'data': results, 'status': 200}
        except Exception as e:
            return {'error': str(e), 'status': 500}
        
    def get_rating_provider(self, provider_name):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = """
                    SELECT 
                        ROUND(AVG(b.rating), 2) AS average_rating,
                        COUNT(DISTINCT b.booking_id) AS total_reviewers
                    FROM 
                        bookings AS a
                        JOIN reviews AS b ON a.id = b.booking_id
                    WHERE 
                        a.provider_name = %s;
                """
            cursor.execute(sql, (provider_name,))
            results = cursor.fetchone()
            cursor.close()
            results['average_rating'] = float(results['average_rating']) if results['average_rating'] != None else 0
            results['total_reviewers'] = (results['total_reviewers']) if results['total_reviewers'] != None else 0

            if not results:
                return {'error': 'No data found', 'status': 404}
            return {'data': results, 'status': 200}
        except Exception as e:
            return {'error': str(e), 'status': 500}


    def get_information_provider(self, provider_name):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = """
                SELECT 
                    ro.option_text,
                    COUNT(rs.id) AS selection_count
                FROM 
                    review_selections rs
                JOIN 
                    reviews r ON rs.review_id = r.id
                JOIN 
                    review_options ro ON rs.option_id = ro.id
                JOIN 
                    bookings b ON r.booking_id = b.id  
                WHERE 
                    r.rating = 5 AND b.provider_name = %s
                GROUP BY 
                    ro.option_text;
                    """
            cursor.execute(sql, (provider_name,))
            results = cursor.fetchall()
            return {'data': results, 'status': 200}
        except Exception as e:
            return {'error': str(e), 'status': 500}
    def add_review_selection(self, option_ids, inserted_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = "INSERT INTO review_selections (`review_id`, `option_id`) VALUES (%s, %s)"
            for option_id in option_ids:
                cursor.execute(sql, (inserted_id, option_id))
            self.connection.commit()
            cursor.close()
            return {'success': True}
        except Exception as e:
            return {'error': str(e), 'success': False}
    def check_booking_exists(self, booking_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = "SELECT * FROM `bookings` WHERE id=%s"
            cursor.execute(sql, (booking_id,))
            booking = cursor.fetchone()
            cursor.close()
            return booking is not None
        except Exception as e:
            error_message = str(e)
            return False
    
    def get_completed_booking(self, user_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            # SQL to get completed bookings that do not have a review yet
            sql = """
                SELECT 
                    b.id AS booking_id, 
                    b.booking_type,
                    ro.id AS review_option_id, 
                    ro.option_text
                FROM 
                    bookings b
                LEFT JOIN 
                    reviews r ON b.id = r.booking_id
                JOIN 
                    review_options ro ON ro.provider_type = b.booking_type
                WHERE 
                    b.user_id = %s 
                    AND b.status = 'completed'
                    AND r.id IS NULL;
            """
            cursor.execute(sql, (user_id,))
            results = cursor.fetchall()
            cursor.close()

            if not results:
                return {'error': 'No completed bookings without reviews found', 'status': 404}
            return {'data': results, 'status': 200}
        except Exception as e:
            return {'error': str(e), 'status': 500}


    def __del__(self):
        self.connection.close()


class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="database_pool",
                pool_size=10,
                pool_reset_session=True,
                host='booking-mysql',
                port="3306",
                database='microservices_soa_h_2',
                user='root',
                password='password'
            )
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
