from nameko.rpc import rpc

import booking.dependencies as sql_dependencies

class BookingService:

    name = 'booking_service'

    database = sql_dependencies.Database()

    @rpc
    def get_all_bookings(self):
        bookings = self.database.get_all_bookings()
        return bookings

    @rpc
    def get_booking_by_id(self, user_id):
        bookings = self.database.get_booking_by_id(user_id = user_id)
        return bookings
    @rpc
    def get_booking_details(self, booking_id):
        bookings = self.database.get_booking_details(booking_id = booking_id)
        return bookings
    
    @rpc
    def add_booking_hotel(self,  user_id, type, total_price, asuransi_id, provider_name,
                    room_type, check_in_date, check_out_date,number_of_rooms,service_id):
        response = self.database.add_booking_hotel(
        user_id=user_id, type=type, total_price=total_price, asuransi_id=asuransi_id, provider_name=provider_name,
        room_type=room_type, check_in_date=check_in_date, check_out_date=check_out_date,number_of_rooms=number_of_rooms,service_id=service_id
        )
        return response
    @rpc
    def add_booking_airline(self,  user_id, type, total_price, asuransi_id, flight_id,flight_date, provider_name,service_id):
        response = self.database.add_booking_airline(
        user_id=user_id, type=type, total_price=total_price, asuransi_id=asuransi_id, flight_id=flight_id, flight_date=flight_date,provider_name=provider_name,service_id=service_id
        )
        return response
    @rpc
    def add_booking_rental(self,  user_id, type, total_price, asuransi_id, provider_name,car_id,pick_up_date,return_date,pick_up_location,return_location,is_with_driver,service_id):
        response = self.database.add_booking_rental(
        user_id=user_id, type=type, total_price=total_price, asuransi_id=asuransi_id, provider_name=provider_name,
                    car_id=car_id, pick_up_date=pick_up_date, return_date=return_date,pick_up_location=pick_up_location,return_location=return_location,
                    is_with_driver=is_with_driver,service_id=service_id)
        return response
    @rpc
    def add_booking_attraction(self,  user_id, type, total_price, asuransi_id, provider_name,
                    paket_attraction_id, visit_date, number_of_tickets,service_id):
        response = self.database.add_booking_attraction(
        user_id=user_id, type=type, total_price=total_price, asuransi_id=asuransi_id, provider_name=provider_name,
        paket_attraction_id=paket_attraction_id, visit_date=visit_date, number_of_tickets=number_of_tickets,service_id=service_id)
        return response
    @rpc
    def edit_booking(self,status,booking_id):
        response = self.database.edit_booking(status = status, booking_id = booking_id)
        return response
    @rpc
    def getCountBookHotel(self):
        response = self.database.getCountBookHotel()
        return response
    @rpc
    def getCountBookAirline(self):
        response = self.database.getCountBookAirline()
        return response
    @rpc
    def getCountBookRental(self):
        response = self.database.getCountBookRental()
        return response
    @rpc
    def getCountBookAttraction(self):
        response = self.database.getCountBookAttraction()
        return response

# Method to add a room
# add_room(self, room_num, room_type)

# Method to change a room's status (0 to 1, or vice versa)
# change_room_status(self, room_num)

# Method to delete a room
# delete_room(self, room_num)

# Notes: you may replace room_num with id
