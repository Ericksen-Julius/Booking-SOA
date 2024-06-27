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
        
    def get_review_date(self, booking_id, booking_type):
        try:
            cursor = self.connection.cursor(dictionary=True)
            result = {}
            # result['date'] = booking_id
            if booking_type == 'Hotel':
                sql = 'SELECT check_out_date FROM booking_hotels WHERE booking_id = %s'
            elif booking_type == 'Airline':
                sql = 'SELECT flight_date FROM booking_airlines WHERE booking_id = %s'
            elif booking_type == 'Attraction':
                sql = 'SELECT visit_date FROM booking_attractions WHERE booking_id = %s'
            else:
                sql = 'SELECT return_date FROM booking_rentals WHERE booking_id = %s'
            
            cursor.execute(sql, (booking_id,))
            resultDate = cursor.fetchone()
            if booking_type == 'Hotel':
                result['date'] = resultDate['check_out_date'].isoformat()
            elif booking_type == 'Airline':
                result['date'] = resultDate['flight_date'].isoformat()
            elif booking_type == 'Attraction':
                result['date'] = resultDate['visit_date'].isoformat()
            else:
                result['date'] = resultDate['return_date'].isoformat()

            
            sql = "SELECT * FROM reviews WHERE booking_id = %s"
            cursor.execute(sql, (booking_id,))
            result2 = cursor.fetchone()
            cursor.close()
            result['reviewed'] = True if result2 is not None else False
            
            return {'data': result, 'status': 200}
            
        except Exception as e:
            return {'error': str(e), 'success': False}

    # def get_reviews_by_booking(self, booking_id):
    #     try:
    #         cursor = self.connection.cursor(dictionary=True)
    #         sql = "SELECT * FROM reviews WHERE booking_id = %s"
    #         cursor.execute(sql, (booking_id,))
    #         reviews = cursor.fetchall()
    #         cursor.close()
    #         return reviews
    #     except Exception as e:
    #         error_message = str(e)
    #         return {'error': error_message, 'status': 500}

    # def get_reviews_by_user(self, user_id):
    #     try:
    #         cursor = self.connection.cursor(dictionary=True)
    #         sql = "SELECT * FROM reviews WHERE user_id = %s"
    #         cursor.execute(sql, (user_id,))
    #         reviews = cursor.fetchall()
    #         cursor.close()
    #         return reviews
    #     except Exception as e:
    #         error_message = str(e)
    #         return {'error': error_message, 'status': 500}

    # def edit_review(self, review_id, rating, review_text):
    #     try:
    #         cursor = self.connection.cursor(dictionary=True)
    #         sql = "UPDATE reviews SET rating = %s, comment = %s, updated_at = NOW() WHERE id = %s"
    #         cursor.execute(sql, (rating, review_text, review_id))
    #         self.connection.commit()
    #         self.set_review_as_edited(review_id)
    #         cursor.close()
    #         return {'message': 'Review updated successfully', 'status': 200}
    #     except Exception as e:
    #         error_message = str(e)
    #         return {'error': error_message, 'status': 500}

    # def set_review_as_edited(self, review_id):
    #     try:
    #         cursor = self.connection.cursor(dictionary=True)
    #         sql = "UPDATE reviews SET isEdited = 1 WHERE id = %s"
    #         cursor.execute(sql, (review_id,))
    #         self.connection.commit()
    #         cursor.close()
    #         return {'message': 'Review marked as edited', 'status': 200}
    #     except Exception as e:
    #         error_message = str(e)
    #         return {'error': error_message, 'status': 500}
    # def get_reviews_by_service_type(self, service_type):
    #     connection = self.get_connection(service_type)
    #     cursor = connection.cursor(dictionary=True)
    #     sql = "SELECT * FROM reviews"
    #     cursor.execute(sql)
    #     reviews = cursor.fetchall()
    #     cursor.close()
    #     connection.close()
    #     return reviews

    # def get_average_rating_by_service_type(self, service_type):
    #     connection = self.get_connection(service_type)
    #     cursor = connection.cursor(dictionary=True)
    #     sql = "SELECT rating FROM reviews"
    #     cursor.execute(sql)
    #     ratings = [row['rating'] for row in cursor.fetchall()]
    #     cursor.close()
    #     connection.close()
    #     if ratings:
    #         return mean(ratings)
    #     else:
    #         return 0
        
    # # Refund related methods
    # def trigger_refund(self, booking_id, user_id, refund_reason):
    #     try:
    #         if not self.check_booking_exists(booking_id):
    #             return {'error': 'Booking does not exist', 'status': 404}

    #         calculate_refund = self.calculate_refund(booking_id)
    #         if 'error' in calculate_refund:
    #             return {'error': 'Error in Calculating Refund', 'status': 400}

    #         refund_amount = calculate_refund['refund_amount']
    #         refund_penalty = calculate_refund['refund_penalty']
    #         cursor = self.connection.cursor(dictionary=True)
            
    #         sql = "INSERT INTO refunds (booking_id, user_id, refund_reason, refund_penalty, refund_amount, refund_status, created_at) VALUES (%s, %s, %s, %s, 'pending', NOW())"
    #         cursor.execute(sql, (booking_id, user_id, refund_reason, refund_penalty, refund_amount))
    #         self.connection.commit()
    #         cursor.close()
    #         return {'message': 'Refund triggered successfully', 'status': 200}
    #     except Exception as e:
    #         error_message = str(e)
    #         return {'error': error_message, 'status': 500}
        
    # def validate_refund(self, booking_id):
    #     try:
    #         cursor = self.connection.cursor(dictionary=True)
    #         sql = "SELECT * FROM bookings WHERE id = %s"
    #         cursor.execute(sql, (booking_id,))
    #         booking = cursor.fetchone()
    #         cursor.close()

    #         if not booking:
    #             return {'error': 'Booking does not exist', 'status': 404}

    #         booking_date = booking['booking_date']
    #         days_until_booking = (booking_date - datetime.now()).days

    #         if days_until_booking > 30:
    #             penalty_rate = 0.25
    #         elif 15 <= days_until_booking <= 30:
    #             penalty_rate = 0.50
    #         elif 7 <= days_until_booking < 15:
    #             penalty_rate = 0.75
    #         else:
    #             penalty_rate = 1.00

    #         return {'penalty_rate': penalty_rate, 'status': 200}
    #     except Exception as e:
    #         error_message = str(e)
    #         return {'error': error_message, 'status': 500}

    # def calculate_refund(self, booking_id):
    #     validation_result = self.validate_refund(booking_id)
    #     if 'error' in validation_result:
    #         return validation_result

    #     penalty_rate = validation_result['penalty_rate']
    #     try:
    #         cursor = self.connection.cursor(dictionary=True)
    #         sql = "SELECT total_price FROM bookings WHERE id = %s"
    #         cursor.execute(sql, (booking_id,))
    #         booking = cursor.fetchone()
    #         cursor.close()

    #         total_price = booking['total_price']
    #         refund_penalty = penalty_rate
    #         refund_amount = total_price * refund_penalty

    #         return {'refund_penalty': refund_penalty, 'refund_amount': refund_amount, 'status': 200}
    #     except Exception as e:
    #         error_message = str(e)
    #         return {'error': error_message, 'status': 500}
        
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
    
    # def get_refunds_by_booking(self, booking_id):
    #     try:
    #         cursor = self.connection.cursor(dictionary=True)
    #         sql = "SELECT * FROM refunds WHERE booking_id = %s"
    #         cursor.execute(sql, (booking_id,))
    #         refunds = cursor.fetchall()
    #         cursor.close()
            
    #         return refunds
    #     except Exception as e:
    #         error_message = str(e)
    #         return {'error': error_message, 'status': 500}

    # def get_refunds_by_user(self, user_id):
    #     try:
    #         cursor = self.connection.cursor(dictionary=True)
    #         sql = "SELECT * FROM refunds WHERE user_id = %s"
    #         cursor.execute(sql, (user_id,))
    #         refunds = cursor.fetchall()
    #         cursor.close()
    #         return refunds
    #     except Exception as e:
    #         error_message = str(e)
    #         return {'error': error_message, 'status': 500}

    # def edit_refunds(self, refund_id, status, refund_amount):
    #     try:
    #         cursor = self.connection.cursor(dictionary=True)
    #         sql = "UPDATE refunds SET status = %s, refund_amount = %s, updated_at = NOW() WHERE id = %s"
    #         cursor.execute(sql, (status, refund_amount, refund_id))
    #         self.connection.commit()
    #         cursor.close()
    #         return {'message': 'Refund updated successfully', 'status': 200}
    #     except Exception as e:
    #         error_message = str(e)
    #         return {'error': error_message, 'status': 500}
        
    
    def get_review_options(self, booking_type):
        try:
            cursor = self.connection.cursor(dictionary=True)
            # SQL to get completed bookings that do not have a review yet
            sql = """
                SELECT rating_group,option_text FROM review_options WHERE provider_type = %s;
            """
            cursor.execute(sql, (booking_type,))
            results = cursor.fetchall()
            cursor.close()

            if not results:
                return {'error': 'No review options available', 'status': 404}
            return {'data': results, 'status': 200}
        except Exception as e:
            return {'error': str(e), 'status': 500}
    def get_review_comment(self, provider_name):
        try:
            cursor = self.connection.cursor(dictionary=True)
            # SQL to get completed bookings that do not have a review yet
            sql = """
                SELECT a.user_id,r.comment,r.rating FROM bookings AS a JOIN reviews AS r ON a.id = r.booking_id WHERE a.provider_name = %s
            """
            cursor.execute(sql, (provider_name,))
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
                database='microservices_soa_h',
                user='root',
                password='password'
            )
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
