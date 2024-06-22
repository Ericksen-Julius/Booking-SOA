from nameko.extensions import DependencyProvider
import json

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from datetime import datetime, timedelta
import random
import string, mean
from datetime import date
# from statistics import mean


def generate_string():
    letters_part = ''.join(random.choices(string.ascii_uppercase, k=3))
    digits_part = ''.join(random.choices(string.digits, k=2))
    return letters_part + digits_part

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection
        
    # Refund related methods
    def trigger_refund(self, booking_id, user_id, refund_reason):
        try:
            if not self.check_booking_exists(booking_id):
                return {'error': 'Booking does not exist', 'status': 404}

            calculate_refund = self.calculate_refund(booking_id)
            if 'error' in calculate_refund:
                return {'error': 'Error in Calculating Refund', 'status': 400}

            refund_amount = calculate_refund['refund_amount']
            refund_penalty = calculate_refund['refund_penalty']
            cursor = self.connection.cursor(dictionary=True)
            
            sql = "INSERT INTO refunds (booking_id, user_id, refund_reason, refund_penalty, refund_amount, refund_status, created_at) VALUES (%s, %s, %s, %s, 'pending', NOW())"
            cursor.execute(sql, (booking_id, user_id, refund_reason, refund_penalty, refund_amount))
            self.connection.commit()
            cursor.close()
            return {'message': 'Refund triggered successfully', 'status': 200}
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}
        
    def validate_refund(self, booking_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = "SELECT * FROM bookings WHERE id = %s"
            cursor.execute(sql, (booking_id,))
            booking = cursor.fetchone()
            cursor.close()

            if not booking:
                return {'error': 'Booking does not exist', 'status': 404}

            booking_date = booking['booking_date']
            days_until_booking = (booking_date - datetime.now()).days

            if days_until_booking > 30:
                penalty_rate = 0.25
            elif 15 <= days_until_booking <= 30:
                penalty_rate = 0.50
            elif 7 <= days_until_booking < 15:
                penalty_rate = 0.75
            else:
                penalty_rate = 1.00

            return {'penalty_rate': penalty_rate, 'status': 200}
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}

    def calculate_refund(self, booking_id):
        validation_result = self.validate_refund(booking_id)
        if 'error' in validation_result:
            return validation_result

        penalty_rate = validation_result['penalty_rate']
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = "SELECT total_price FROM bookings WHERE id = %s"
            cursor.execute(sql, (booking_id,))
            booking = cursor.fetchone()
            cursor.close()

            total_price = booking['total_price']
            refund_penalty = penalty_rate
            refund_amount = total_price * refund_penalty

            return {'refund_penalty': refund_penalty, 'refund_amount': refund_amount, 'status': 200}
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}
        
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
    
    def get_refunds_by_booking(self, booking_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = "SELECT * FROM refunds WHERE booking_id = %s"
            cursor.execute(sql, (booking_id,))
            refunds = cursor.fetchall()
            cursor.close()
            
            return refunds
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}

    def get_refunds_by_user(self, user_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = "SELECT * FROM refunds WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            refunds = cursor.fetchall()
            cursor.close()
            return refunds
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}

    def edit_refunds(self, refund_id, status, refund_amount):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = "UPDATE refunds SET status = %s, refund_amount = %s, updated_at = NOW() WHERE id = %s"
            cursor.execute(sql, (status, refund_amount, refund_id))
            self.connection.commit()
            cursor.close()
            return {'message': 'Refund updated successfully', 'status': 200}
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}
        
    


    def send_data_to_payment(self, booking_id):
        # Implement communication with payment microservice
        pass

    def send_data_to_accomodation(self, booking_id):
        # Implement communication with provider
        pass

    def send_data_to_notification(self, booking_id):
        # Implement notification
        pass



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
