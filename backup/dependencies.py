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
                'booking_code': row['booking_code'],
                'provider_name': row['provider_name'],
                'booking_type': row['booking_type'],
                'total_price': float(row['total_price']),
                'asuransi_id': row['asuransi_id']
            })
        cursor.close()
        return result
    
    def get_booking_by_id(self, user_id):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM bookings WHERE user_id = %s"
        cursor.execute(sql,(user_id,))
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'booking_date': row['booking_date'].strftime("%Y-%m-%d %H:%M:%S"),
                'status': row['status'],
                'booking_code': row['booking_code'],
                'provider_name': row['provider_name'],
                'booking_type': row['booking_type'],
                'total_price': float(row['total_price']),
                'asuransi_id': row['asuransi_id']
            })
        cursor.close()
        return result
    
    def get_booking_details(self, booking_id):    
        try:    
            cursor = self.connection.cursor(dictionary=True)
            sql = "SELECT booking_type FROM bookings WHERE id = %s"
            cursor.execute(sql,(booking_id,))
            result = cursor.fetchone()
            if (result and result['booking_type'] == "Hotel"):
                sql = """
                SELECT 
                    a.service_id,
                    b.room_type,
                    a.provider_name,
                    a.booking_code,
                    b.check_in_date,
                    b.check_out_date,
                    b.number_of_rooms,
                    DATEDIFF(b.check_out_date, b.check_in_date) AS number_of_nights
                FROM 
                    bookings AS a
                LEFT JOIN 
                    booking_hotels AS b 
                ON 
                    a.id = b.booking_id 
                WHERE 
                    a.id = %s;
                """
                cursor.execute(sql,(booking_id,))
                bookings = cursor.fetchone()
                if bookings:
                    if isinstance(bookings['check_in_date'], date):
                        bookings['check_in_date'] = bookings['check_in_date'].isoformat()
                    if isinstance(bookings['check_out_date'], date):
                        bookings['check_out_date'] = bookings['check_out_date'].isoformat()
            elif (result and result['booking_type'] == "Airline"):
                sql = """
                SELECT 
                    a.service_id,
                    a.booking_code,
                    a.provider_name,
                    a.asuransi_id,
                    b.flight_id,
                    b.flight_date
                FROM 
                    bookings AS a
                LEFT JOIN 
                    booking_airlines AS b 
                ON 
                    a.id = b.booking_id 
                WHERE 
                    a.id = %s;
                """
                cursor.execute(sql,(booking_id,))
                bookings = cursor.fetchone()
                if bookings:
                    if isinstance(bookings['flight_date'], date):
                        bookings['flight_date'] = bookings['flight_date'].isoformat()
            elif (result and result['booking_type'] == "Rental"):
                sql = """
                SELECT 
                    a.service_id,
                    a.booking_code,
                    a.provider_name,
                    a.asuransi_id,
                    b.pickup_date,
                    b.return_date,
                    b.car_id,
                    b.pickup_location,
                    b.return_location,
                    b.is_with_driver
                FROM 
                    bookings AS a
                LEFT JOIN 
                    booking_rentals AS b 
                ON 
                    a.id = b.booking_id 
                WHERE 
                    a.id = %s;
                """
                cursor.execute(sql,(booking_id,))
                bookings = cursor.fetchone()
                if bookings:
                    if isinstance(bookings['pickup_date'], date):
                        bookings['pickup_date'] = bookings['pickup_date'].isoformat()
                    if isinstance(bookings['return_date'], date):
                        bookings['return_date'] = bookings['return_date'].isoformat()
            elif (result and result['booking_type'] == "Attraction"):
                sql = """
                SELECT 
                    a.service_id,
                    a.booking_code,
                    a.provider_name,
                    b.visit_date,
                    b.paket_attraction_id
                FROM 
                    bookings AS a
                LEFT JOIN 
                    booking_attractions AS b 
                ON 
                    a.id = b.booking_id 
                WHERE 
                    a.id = %s;
                """
                cursor.execute(sql,(booking_id,))
                bookings = cursor.fetchone()
                if bookings:
                    if isinstance(bookings['visit_date'], date):
                        bookings['visit_date'] = bookings['visit_date'].isoformat()
            return {'booking details': bookings}
        except Exception as e:
                error_message = str(e)
                return {'error': error_message}


    def add_booking_hotel(self,user_id, type, total_price, asuransi_id, provider_name,
        room_type, check_in_date, check_out_date,number_of_rooms,service_id):
        result = self.add_booking(user_id=user_id,type=type,total_price=total_price,asuransi_id=asuransi_id ,provider_name=provider_name,service_id=service_id)
        if(result['success']):
            try:
                cursor = self.connection.cursor(dictionary=True)
                sql = "INSERT INTO `booking_hotels`(`booking_id`, `room_type`, `check_in_date`, `check_out_date`, `number_of_rooms`) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (result['new_inserted_id'],room_type,check_in_date,check_out_date,number_of_rooms))
                self.connection.commit()
                data = {}
                data['type'] = type
                data['provider_name'] = provider_name
                data['check_in_date'] = check_in_date
                data['check_out_date'] = check_out_date
                data['number_of_rooms'] = number_of_rooms
                data['booking_code'] = result['booking_code']
                cursor.close()
                return {'message': 'Booking created successfully','status': 200, 'data': data, 'booking_code': result['booking_code'],'booking_id': result['new_inserted_id'] }
            except Exception as e:
                error_message = str(e)
                return {'error': error_message}
        else:
            return {'error': result['error']}
        
    def add_booking_airline(self,user_id, type, total_price, asuransi_id, flight_id, flight_date,provider_name,service_id):
        result = self.add_booking(user_id=user_id,type=type,total_price=total_price,asuransi_id=asuransi_id, provider_name=provider_name,service_id=service_id)
        if(result['success']):
            try:
                cursor = self.connection.cursor(dictionary=True)
                sql = "INSERT INTO `booking_airlines`(`booking_id`, `flight_id` ,`flight_date`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (result['new_inserted_id'],flight_id,flight_date))
                self.connection.commit()
                data = {}
                data['type'] = type
                data['provider_name'] = provider_name
                data['flight_id'] = flight_id
                data['flight_date'] = flight_date
                data['booking_code'] = result['booking_code']
                cursor.close()
                return {'message': 'Booking created successfully','status': 200, "data": data, 'booking_code': result['booking_code']}
            except Exception as e:
                error_message = str(e)
                return {'error': error_message}
        else:
            return {'error': result['error']}
        
    def add_booking_rental(self,user_id, type, total_price, asuransi_id, provider_name,car_id,pick_up_date,return_date,pick_up_location,
        return_location,is_with_driver,service_id):
        result = self.add_booking(user_id=user_id,type=type,total_price=total_price,asuransi_id=asuransi_id, provider_name=provider_name,service_id=service_id)
        if(result['success']):
            try:
                cursor = self.connection.cursor(dictionary=True)
                sql = "INSERT INTO `booking_rentals`(`booking_id`, `car_id`, `pickup_date`, `return_date`, `pickup_location`, `return_location`, `is_with_driver`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (result['new_inserted_id'],car_id,pick_up_date,return_date,pick_up_location,return_location,is_with_driver))
                self.connection.commit()
                inserted_id = cursor.lastrowid
                data = {}
                data['type'] = type
                data['provider_name'] = provider_name
                data['car_id'] = car_id
                data['pick_up_date'] = pick_up_date
                data['return_date'] = return_date
                data['pick_up_location'] = pick_up_location
                data['return_location'] = return_location
                data['is_with_driver'] = is_with_driver
                data['booking_code'] = result['booking_code']
                cursor.close()
                return {'message': 'Booking created successfully','status': 200 , 'data': data, 'booking_code': result['booking_code'],'booking_id':  result['new_inserted_id']}
            except Exception as e:
                error_message = str(e)
                return {'error': error_message}
        else:
            return {'error': result['error']}
        
    def add_booking_attraction(self,user_id, type, total_price, asuransi_id, provider_name,
        paket_attraction_id, visit_date, number_of_tickets,service_id):
        result = self.add_booking(user_id=user_id,type=type,total_price=total_price,asuransi_id=asuransi_id, provider_name=provider_name,service_id=service_id)
        if(result['success']):
            try:
                cursor = self.connection.cursor(dictionary=True)
                sql = "INSERT INTO `booking_attractions`(`booking_id`, `paket_attraction_id`, `visit_date`, `number_of_tickets`) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (result['new_inserted_id'],paket_attraction_id,visit_date,number_of_tickets))
                self.connection.commit()
                inserted_id = cursor.lastrowid
                data = {}
                data['type'] = type
                data['provider_name'] = provider_name
                data['paket_attraction_id'] = paket_attraction_id
                data['visit_date'] = visit_date
                data['number_of_tickets'] = number_of_tickets
                data['booking_code'] = result['booking_code']
                cursor.close()
                return {'message': 'Booking created successfully','status': 200, 'data': data, 'booking_code': result['booking_code'],'booking_id': result['new_inserted_id']}
            except Exception as e:
                error_message = str(e)
                return {'error': error_message}
        else:
            return {'error': result['error']}
        
    def add_booking(self,user_id, type, total_price, asuransi_id,provider_name,service_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            while(True):
                random_code = generate_string()
                booking_code = f'{type[0]}{random_code}'
                check_sql = "SELECT * FROM `bookings` WHERE booking_code = %s"
                cursor.execute(check_sql,(booking_code,))
                exist_code = cursor.fetchone()
                if exist_code is None:
                    break
            sql = "INSERT INTO `bookings`(`user_id`, `booking_type`, `booking_code`,`total_price`, `asuransi_id` ,`provider_name`, `service_id`) VALUES (%s,%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user_id, type, booking_code, total_price, asuransi_id, provider_name, service_id))
            self.connection.commit()
            inserted_id = cursor.lastrowid
            cursor.close()
            return {'success': True, 'new_inserted_id': inserted_id, 'booking_code' : booking_code}
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'success': False}
        
    def edit_booking(self,status,booking_code):
        try:
            cursor = self.connection.cursor(dictionary=True)

            check_sql = "SELECT * FROM `bookings` WHERE booking_code=%s"
            cursor.execute(check_sql, (booking_code,))
            existing_booking = cursor.fetchone()

            if existing_booking is None:
                return {'message': f'Booking with code {booking_code} does not exist in the database','status': 404}
            sql = "UPDATE `bookings` SET `status`=%s WHERE booking_code=%s"
            cursor.execute(sql, (status,booking_code))
            self.connection.commit()
            cursor.close()
            return {'message': 'Booking updated successfully','status': 200}
        except Exception as e:
            error_message = str(e)
            return {'error': error_message}
        
    def getCountBookHotel(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            result = []
            sql = "SELECT provider_name, COUNT(*) AS booking_count FROM bookings WHERE booking_type = 'Hotel' GROUP BY provider_name;"
            cursor.execute(sql)
            for row in cursor.fetchall():
                result.append({
                    'hotel_name': row['provider_name'],
                    'booking_count': row['booking_count'],
                })
            cursor.close()
            return result
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}
    def getCountBookAirline(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            result = []
            sql = "SELECT provider_name, COUNT(*) AS booking_count FROM bookings WHERE booking_type = 'Airline' GROUP BY provider_name;"
            cursor.execute(sql)
            for row in cursor.fetchall():
                result.append({
                    'airline_name': row['provider_name'],
                    'booking_count': row['booking_count'],
                })
            cursor.close()
            return result
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}
    def getCountBookRental(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            result = []
            sql = "SELECT provider_name, COUNT(*) AS booking_count FROM bookings WHERE booking_type = 'Rental' GROUP BY provider_name;"
            cursor.execute(sql)
            for row in cursor.fetchall():
                result.append({
                    'rental_name': row['provider_name'],
                    'booking_count': row['booking_count'],
                })
            cursor.close()
            return result
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}
        
    def getCountBookAttraction(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            result = []
            sql = "SELECT provider_name, COUNT(*) AS booking_count FROM bookings WHERE booking_type = 'Attraction' GROUP BY provider_name;"
            cursor.execute(sql)
            for row in cursor.fetchall():
                result.append({
                    'attraction_name': row['provider_name'],
                    'booking_count': row['booking_count'],
                })
            cursor.close()
            return result
        except Exception as e:
            error_message = str(e)
            return {'error': error_message, 'status': 500}
        

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


    # def add_review_selection(self, option_ids, inserted_id):
    #     try:
    #         cursor = self.connection.cursor(dictionary=True)
    #         sql = "INSERT INTO review_selections (`review_id`, `option_id`) VALUES (%s, %s)"
    #         for option_id in option_ids:
    #             cursor.execute(sql, (inserted_id, option_id))
    #         self.connection.commit()
    #         cursor.close()
    #         return {'success': True}
    #     except Exception as e:
    #         return {'error': str(e), 'success': False}

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
        
    # def check_booking_exists(self, booking_id):
    #     try:
    #         cursor = self.connection.cursor(dictionary=True)
    #         sql = "SELECT * FROM `bookings` WHERE id=%s"
    #         cursor.execute(sql, (booking_id,))
    #         booking = cursor.fetchone()
    #         cursor.close()
    #         return booking is not None
    #     except Exception as e:
    #         error_message = str(e)
    #         return False
    
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
        
    


    # def send_data_to_payment(self, booking_id):
    #     # Implement communication with payment microservice
    #     pass

    # def send_data_to_accomodation(self, booking_id):
    #     # Implement communication with provider
    #     pass

    # def send_data_to_notification(self, booking_id):
    #     # Implement notification
    #     pass



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
