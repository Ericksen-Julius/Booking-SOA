import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http



class GatewayService:
    name = 'gateway'

    booking_rpc = RpcProxy('booking_service')

    @http('GET', '/booking')
    def get_all_bookings(self, request):
        rooms = self.booking_rpc.get_all_bookings()
        return json.dumps(rooms)
    
    @http('POST', '/booking')
    def add_booking(self, request):
        try:
            data = request.get_data(as_text=True)
            booking_data = json.loads(data)
            user_id = booking_data.get('user_id')
            type = booking_data.get('type')
            total_price = booking_data.get('total_price')
            asuransi_id = booking_data.get('asuransi_id') if 'asuransi_id' in booking_data else None
            if(type == "Hotel"):
                hotel_name = booking_data.get('hotel_name')
                room_type = booking_data.get('room_type')
                check_in_date = booking_data.get('check_in_date')
                check_out_date = booking_data.get('check_out_date')
                number_of_rooms = booking_data.get('number_of_rooms')
                response = self.booking_rpc.add_booking_hotel(
                    user_id=user_id, type=type, total_price=total_price, asuransi_id=asuransi_id, hotel_name=hotel_name,
                    room_type=room_type, check_in_date=check_in_date, check_out_date=check_out_date,number_of_rooms=number_of_rooms
                )
            elif(type == "Airline"):
                flight_id = booking_data.get('flight_id')
                response = self.booking_rpc.add_booking_airline(
                    user_id=user_id, type=type, total_price=total_price, asuransi_id=asuransi_id, flight_id=flight_id
                )
            elif(type == "Rental"):
                rental_provider_name = booking_data.get('rental_provider_name')
                car_id = booking_data.get('car_id')
                pick_up_date = booking_data.get('pick_up_date')
                return_date = booking_data.get('return_date')
                pick_up_location = booking_data.get('pick_up_location')
                return_location = booking_data.get('return_location')
                is_with_driver = booking_data.get('is_with_driver')
                response = self.booking_rpc.add_booking_rental(
                    user_id=user_id, type=type, total_price=total_price, asuransi_id=asuransi_id, rental_provider_name=rental_provider_name,
                    car_id=car_id, pick_up_date=pick_up_date, return_date=return_date,pick_up_location=pick_up_location,return_location=return_location,
                    is_with_driver=is_with_driver
                )  
            else:
                attraction_provider_name = booking_data.get('attraction_provider_name')
                paket_attraction_id = booking_data.get('paket_attraction_id')
                visit_date = booking_data.get('visit_date')
                number_of_tickets = booking_data.get('number_of_tickets')
                response = self.booking_rpc.add_booking_attraction(
                    user_id=user_id, type=type, total_price=total_price, asuransi_id=asuransi_id, attraction_provider_name=attraction_provider_name,
                    paket_attraction_id=paket_attraction_id, visit_date=visit_date, number_of_tickets=number_of_tickets
                )  

            return response['status'],response['message']
        except Exception as e:
            error_message = str(e)
            return 500,json.dumps({'error': error_message})
    @http('PUT', '/booking/<int:booking_id>')
    def edit_booking(self, request,booking_id):
        try:
            data = request.get_data(as_text=True)
            json_data = json.loads(data)
            status = json_data.get('status')
            response = self.booking_rpc.edit_booking(status=status, booking_id=booking_id)

            return response['status'],response['message']

        except Exception as e:
            error_message = str(e)
            return 500,json.dumps({'error': error_message}) 

