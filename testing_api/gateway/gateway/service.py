import json

from marshmallow import ValidationError
from nameko import config
from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService(object):
    """
    Service acts as a gateway to other services over http.
    """

    name = 'gateway'

    header = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "*",     
        "Access-Control-Allow-Headers": "*",     
    }

    booking_rpc = RpcProxy('booking_service')

    @http('GET', '/booking')
    def get_all_bookings(self, request):
        bookings = self.booking_rpc.get_all_bookings()
        return (200, self.header, json.dumps(bookings))
    
    @http('GET', '/booking/<int:user_id>')
    def get_booking_by_id(self, request, user_id):
        try:
            # return 200, str(cuy)
            bookings = self.booking_rpc.get_booking_by_id(user_id=user_id)
            
            if bookings:
                return 200, self.header, json.dumps(bookings)
            return 400, self.header ,"Booking not found"
        except Exception as e:
            return 500, str(e)
    @http('GET', '/bookingDetails/<int:booking_id>')
    def get_booking_details(self, request, booking_id):
        try:
            bookings = self.booking_rpc.get_booking_details(booking_id=booking_id)
            if bookings:
                return 200, self.header, json.dumps(bookings)
            return 400, self.header ,"Booking not found"
        except Exception as e:
            return 500, str(e)
        
    
    @http('POST', '/booking')
    def add_booking(self, request):
        try:
            data = request.get_data(as_text=True)
            booking_data = json.loads(data)
            user_id = booking_data.get('user_id')
            type = booking_data.get('type')
            total_price = booking_data.get('total_price')
            service_id = booking_data.get('service_id')
            provider_name = booking_data.get('provider_name')
            asuransi_id = booking_data.get('asuransi_id') if 'asuransi_id' in booking_data else None
            if(type == "Hotel"):
                room_type = booking_data.get('room_type')
                check_in_date = booking_data.get('check_in_date')
                check_out_date = booking_data.get('check_out_date')
                number_of_rooms = booking_data.get('number_of_rooms')
                response = self.booking_rpc.add_booking_hotel(
                    user_id=user_id, type=type, total_price=total_price, asuransi_id=asuransi_id, provider_name=provider_name,
                    room_type=room_type, check_in_date=check_in_date, check_out_date=check_out_date,number_of_rooms=number_of_rooms,
                    service_id=service_id
                )
            elif(type == "Airline"):
                flight_id = booking_data.get('flight_id')
                flight_date = booking_data.get('flight_date')
                response = self.booking_rpc.add_booking_airline(
                    user_id=user_id, type=type, total_price=total_price, asuransi_id=asuransi_id,flight_id=flight_id, flight_date=flight_date,
                    provider_name=provider_name, service_id=service_id
                )
            elif(type == "Rental"):
                car_id = booking_data.get('car_id')
                pick_up_date = booking_data.get('pick_up_date')
                return_date = booking_data.get('return_date')
                pick_up_location = booking_data.get('pick_up_location')
                return_location = booking_data.get('return_location')
                is_with_driver = booking_data.get('is_with_driver')
                response = self.booking_rpc.add_booking_rental(
                    user_id=user_id, type=type, total_price=total_price, asuransi_id=asuransi_id, provider_name=provider_name,
                    car_id=car_id, pick_up_date=pick_up_date, return_date=return_date,pick_up_location=pick_up_location,return_location=return_location,
                    is_with_driver=is_with_driver,service_id=service_id
                )  
            else:
                paket_attraction_id = booking_data.get('paket_attraction_id')
                visit_date = booking_data.get('visit_date')
                number_of_tickets = booking_data.get('number_of_tickets')
                response = self.booking_rpc.add_booking_attraction(
                    user_id=user_id, type=type, total_price=total_price, asuransi_id=asuransi_id, provider_name=provider_name,
                    paket_attraction_id=paket_attraction_id, visit_date=visit_date, number_of_tickets=number_of_tickets,service_id=service_id
                )  

            return (response['status'],self.header ,json.dumps(response))
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

            return (response['status'],self.header,response['message'])

        except Exception as e:
            error_message = str(e)
            return 500,json.dumps({'error': error_message}) 

    @http('GET', '/booking/getCountBookHotel')
    def getCountBookHotel(self, request):
        try:
            data = self.booking_rpc.getCountBookHotel()
            return (200, self.header, json.dumps(data))
        except Exception as e:
            error_message = str(e)
            return 500,json.dumps({'error': error_message})
    @http('GET', '/booking/getCountBookAirline')
    def getCountBookAirline(self, request):
        try:
            data = self.booking_rpc.getCountBookAirline()
            return (200,self.header,json.dumps(data))
        except Exception as e:
            error_message = str(e)
            return 500,json.dumps({'error': error_message})
    @http('GET', '/booking/getCountBookRental')
    def getCountBookRental(self, request):
        try:
            data = self.booking_rpc.getCountBookRental()
            return (200, self.header,json.dumps(data))
        except Exception as e:
            error_message = str(e)
            return 500,json.dumps({'error': error_message})
    @http('GET', '/booking/getCountBookAttraction')
    def getCountBookAttraction(self, request):
        try:
            data = self.booking_rpc.getCountBookAttraction()
            return (200, self.header,json.dumps(data))

        except Exception as e:
            error_message = str(e)
            return 500,json.dumps({'error': error_message})
            
        
        
    @http('POST', '/review')
    def add_review(self, request):
        try:
            data = request.get_data(as_text=True)
            review_data = json.loads(data)
            booking_id = review_data.get('booking_id')
            user_id = review_data.get('user_id')
            rating = review_data.get('rating')
            review_text = review_data.get('review_text')
            response = self.review_rpc.add_review(booking_id, user_id, rating, review_text)
            return response['status'], json.dumps({'message': response['message']})
        except Exception as e:
            error_message = str(e)
            return 500, json.dumps({'error': error_message})

    @http('GET', '/review/booking/<int:booking_id>')
    def get_reviews_by_booking(self, request, booking_id):
        try:
            reviews = self.review_rpc.get_reviews_by_booking(booking_id)
            return 200, json.dumps(reviews)
        except Exception as e:
            error_message = str(e)
            return 500, json.dumps({'error': error_message})

    @http('GET', '/review/user/<int:user_id>')
    def get_reviews_by_user(self, request, user_id):
        try:
            reviews = self.review_rpc.get_reviews_by_user(user_id)
            return 200, json.dumps(reviews)
        except Exception as e:
            error_message = str(e)
            return 500, json.dumps({'error': error_message})

    @http('PUT', '/review/<int:review_id>')
    def edit_review(self, request, review_id):
        try:
            data = request.get_data(as_text=True)
            review_data = json.loads(data)
            rating = review_data.get('rating')
            review_text = review_data.get('review_text')
            response = self.review_rpc.edit_review(review_id, rating, review_text)
            return response['status'], json.dumps({'message': response['message']})
        except Exception as e:
            error_message = str(e)
            return 500, json.dumps({'error': error_message})
    @http("GET", "/reviews/<string:service_type>")
    def get_reviews_and_average(self, request, service_type):
        valid_service_types = ["hotel", "airline", "attraction", "car_rental", "travel_agent"]
        
        if service_type not in valid_service_types:
            return 400, json.dumps({"error": "Invalid service type"})
        
        result = self.review_rpc.get_reviews_and_average_by_service_type(service_type)
        return 200, json.dumps(result)
    
    @http('POST', '/refund')
    def trigger_refund(self, request):
        try:
            data = request.get_data(as_text=True)
            refund_data = json.loads(data)
            booking_id = refund_data.get('booking_id')
            user_id = refund_data.get('user_id')
            refund_reason = refund_data.get('refund_reason')
            response = self.refund_rpc.trigger_refund(booking_id, user_id, refund_reason)
            return response['status'], json.dumps({'message': response['message']})
        except Exception as e:
            error_message = str(e)
            return 500, json.dumps({'error': error_message})

    @http('GET', '/refunds/booking/<int:booking_id>')
    def get_refunds_by_booking(self, request, booking_id):
        refunds = self.refund_rpc.get_refunds_by_booking(booking_id)
        return json.dumps(refunds)

    @http('GET', '/refunds/user/<int:user_id>')
    def get_refunds_by_user(self, request, user_id):
        refunds = self.refund_rpc.get_refunds_by_user(user_id)
        return json.dumps(refunds)

    @http('PUT', '/refunds/<int:refund_id>')
    def edit_refund(self, request, refund_id):
        try:
            data = request.get_data(as_text=True)
            refund_data = json.loads(data)
            status = refund_data.get('status')
            refund_amount = refund_data.get('refund_amount')
            response = self.refund_rpc.edit_refunds_data(refund_id, status, refund_amount)
            return response['status'], json.dumps(response)
        except Exception as e:
            error_message = str(e)
            return 500, json.dumps({'error': error_message})
        
    # @http('GET', '/refund/validate/<int:booking_id>')
    # def validate_refund(self, request, booking_id):
    #     try:
    #         response = self.refund_rpc.validate_refund(booking_id)
    #         return response['status'], json.dumps({'message': response['message']})
    #     except Exception as e:
    #         error_message = str(e)
    #         return 500, json.dumps({'error': error_message})

    # @http('GET', '/refund/calculate/<int:booking_id>')
    # def calculate_refund(self, request, booking_id):
    #     try:
    #         response = self.refund_rpc.calculate_refund(booking_id)
    #         return response['status'], json.dumps({'message': response['message']})
    #     except Exception as e:
    #         error_message = str(e)
    #         return 500, json.dumps({'error': error_message})
