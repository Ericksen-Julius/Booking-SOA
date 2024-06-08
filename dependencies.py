from nameko.extensions import DependencyProvider
import json

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from datetime import datetime, timedelta
import random
import string


def generate_string():
    letters_part = ''.join(random.choices(string.ascii_uppercase, k=3))
    digits_part = ''.join(random.choices(string.digits, k=2))
    return letters_part + digits_part

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection
    

    def get_all_bookings(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM bookings"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'user_id': row['user_id'],
                'booking_date': row['booking_date'].strftime("%Y-%m-%d %H:%M:%S"),
                'status': row['status'],
                'total_price': float(row['total_price']),
                'asuransi_id': row['asuransi_id']
            })
        cursor.close()
        return result

    def add_booking_hotel(self,user_id, type, total_price, asuransi_id, hotel_name,
        room_type, check_in_date, check_out_date,number_of_rooms):
        result = self.add_booking(user_id=user_id,type=type,total_price=total_price,asuransi_id=asuransi_id)
        if(result['success']):
            try:
                cursor = self.connection.cursor(dictionary=True)
                sql = "INSERT INTO `booking_hotels`(`booking_id`, `hotel_name`, `room_type`, `check_in_date`, `check_out_date`, `number_of_rooms`) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (result['new_inserted_id'],hotel_name,room_type,check_in_date,check_out_date,number_of_rooms))
                self.connection.commit()
                cursor.close()
                return {'message': 'Booking created successfully','status': 200}
            except Exception as e:
                error_message = str(e)
                return {'error': error_message}
        else:
            return {'error': result['error']}
        
    def add_booking_airline(self,user_id, type, total_price, asuransi_id, flight_id):
        result = self.add_booking(user_id=user_id,type=type,total_price=total_price,asuransi_id=asuransi_id)
        if(result['success']):
            try:
                cursor = self.connection.cursor(dictionary=True)
                sql = "INSERT INTO `booking_airlines`(`booking_id`, `flight_id`) VALUES (%s, %s)"
                cursor.execute(sql, (result['new_inserted_id'],flight_id))
                self.connection.commit()
                cursor.close()
                return {'message': 'Booking created successfully','status': 200}
            except Exception as e:
                error_message = str(e)
                return {'error': error_message}
        else:
            return {'error': result['error']}
        
    def add_booking_rental(self,user_id, type, total_price, asuransi_id, rental_provider_name,car_id,pick_up_date,return_date,pick_up_location,
        return_location,is_with_driver):
        result = self.add_booking(user_id=user_id,type=type,total_price=total_price,asuransi_id=asuransi_id)
        if(result['success']):
            try:
                cursor = self.connection.cursor(dictionary=True)
                sql = "INSERT INTO `booking_rentals`(`booking_id`, `rental_provider_name`, `car_id`, `pickup_date`, `return_date`, `pickup_location`, `return_location`, `is_with_driver`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (result['new_inserted_id'],rental_provider_name,car_id,pick_up_date,return_date,pick_up_location,return_location,is_with_driver))
                self.connection.commit()
                cursor.close()
                return {'message': 'Booking created successfully','status': 200}
            except Exception as e:
                error_message = str(e)
                return {'error': error_message}
        else:
            return {'error': result['error']}
        
    def add_booking_attraction(self,user_id, type, total_price, asuransi_id, attraction_provider_name,
        paket_attraction_id, visit_date, number_of_tickets):
        result = self.add_booking(user_id=user_id,type=type,total_price=total_price,asuransi_id=asuransi_id)
        if(result['success']):
            try:
                cursor = self.connection.cursor(dictionary=True)
                sql = "INSERT INTO `booking_attractions`(`booking_id`, `attraction_provider_name`, `paket_attraction_id`, `visit_date`, `number_of_tickets`) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (result['new_inserted_id'],attraction_provider_name,paket_attraction_id,visit_date,number_of_tickets))
                self.connection.commit()
                cursor.close()
                return {'message': 'Booking created successfully','status': 200}
            except Exception as e:
                error_message = str(e)
                return {'error': error_message}
        else:
            return {'error': result['error']}
        
    def add_booking(self,user_id, type, total_price, asuransi_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            while(True):
                random_code = generate_string()
                booking_code = f'#{type[0]}{random_code}'
                check_sql = "SELECT * FROM `bookings` WHERE booking_code = %s"
                cursor.execute(check_sql,(booking_code,))
                exist_code = cursor.fetchone()
                if exist_code is None:
                    break
            sql = "INSERT INTO `bookings`(`user_id`, `booking_type`, `booking_code`,`total_price`, `asuransi_id`) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (user_id, type, booking_code, total_price, asuransi_id))
            self.connection.commit()
            inserted_id = cursor.lastrowid
            cursor.close()
            return {'success': True, 'new_inserted_id': inserted_id}
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'success': False}
    def edit_booking(self,status,booking_id):
        try:
            cursor = self.connection.cursor(dictionary=True)

            check_sql = "SELECT * FROM `bookings` WHERE id=%s"
            cursor.execute(check_sql, (booking_id,))
            existing_booking = cursor.fetchone()

            if existing_booking is None:
                return {'message': f'Booking with id {booking_id} does not exist in the database','status': 404}
            sql = "UPDATE `bookings` SET `status`=%s WHERE id=%s"
            cursor.execute(sql, (status,booking_id))
            self.connection.commit()
            cursor.close()
            return {'message': 'Booking updated successfully','status': 200}
        except Exception as e:
            error_message = str(e)
            return {'error': error_message}
        
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



#    def __del__(self):
#        self.connection.close()


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
