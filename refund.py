from nameko.rpc import rpc
import dependencies

class RefundService:

    name = 'refund_service'
    
    database = dependencies.Database()

    # @rpc
    # def trigger_refund(self, booking_id):
    #     response = self.database.trigger_refund(booking_id)
    #     return response

    # @rpc
    # def validate_refund(self, booking_id):
    #     response = self.database.validate_refund(booking_id)
    #     return response

    # @rpc
    # def calculate_refund(self, booking_id):
    #     response = self.database.calculate_refund(booking_id)
    #     return response

    @rpc
    def get_refunds_by_booking(self, booking_id):
        reviews = self.database.get_reviews_by_booking(booking_id)
        return reviews

    @rpc
    def get_refunds_by_user(self, user_id):
        reviews = self.database.get_reviews_by_user(user_id)
        return reviews

    @rpc
    def edit_refunds_data(self, refund_id, status, refund_amount):
        #
        response = self.database.edit_refunds(refund_id, status, refund_amount)
        return response
    #Harusnya ada method/api route yang bisa untuk post data ke service lain
    @rpc
    def send_data_to_paymentServices(self, refund_id, booking_id):
        
        return response
    
    @rpc
    def send_data_to_AccomodationServices(self, refund_id,  booking_id):
        
        return response
    
    @rpc
    def send_data_to_notifServices(self, refund_id, booking_id):
        
        return response