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
    def add_review(self, booking_id, user_id, rating, review_text):
        try:
            if not self.check_booking_exists(booking_id):
                return {'error': 'Booking does not exist', 'status': 404}
            cursor = self.connection.cursor(dictionary=True)
            sql = "INSERT INTO reviews (booking_id, user_id, rating, comment, created_at) VALUES (%s, %s, %s, %s, NOW())"
            cursor.execute(sql, (booking_id, user_id, rating, review_text))
            self.connection.commit()
            cursor.close()
            return {'message': 'Review added successfully', 'status': 200}
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}

    def get_reviews_by_booking(self, booking_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = "SELECT * FROM reviews WHERE booking_id = %s"
            cursor.execute(sql, (booking_id,))
            reviews = cursor.fetchall()
            cursor.close()
            return reviews
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}

    def get_reviews_by_user(self, user_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = "SELECT * FROM reviews WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            reviews = cursor.fetchall()
            cursor.close()
            return reviews
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}

    def edit_review(self, review_id, rating, review_text):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = "UPDATE reviews SET rating = %s, comment = %s, updated_at = NOW() WHERE id = %s"
            cursor.execute(sql, (rating, review_text, review_id))
            self.connection.commit()
            self.set_review_as_edited(review_id)
            cursor.close()
            return {'message': 'Review updated successfully', 'status': 200}
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}

    def set_review_as_edited(self, review_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = "UPDATE reviews SET isEdited = 1 WHERE id = %s"
            cursor.execute(sql, (review_id,))
            self.connection.commit()
            cursor.close()
            return {'message': 'Review marked as edited', 'status': 200}
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}
    def get_reviews_by_service_type(self, service_type):
        connection = self.get_connection(service_type)
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM reviews"
        cursor.execute(sql)
        reviews = cursor.fetchall()
        cursor.close()
        connection.close()
        return reviews

    def get_average_rating_by_service_type(self, service_type):
        connection = self.get_connection(service_type)
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT rating FROM reviews"
        cursor.execute(sql)
        ratings = [row['rating'] for row in cursor.fetchall()]
        cursor.close()
        connection.close()
        if ratings:
            return mean(ratings)
        else:
            return 0
        
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
                host='localhost',
                database='microservices_soa_h',
                user='root',
                password=''
            )
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
