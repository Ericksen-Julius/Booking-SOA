from nameko.extensions import DependencyProvider
import json

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

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
            sql = "INSERT INTO `bookings`(`user_id`, `booking_type`, `total_price`, `asuransi_id`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (user_id, type, total_price, asuransi_id))
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
