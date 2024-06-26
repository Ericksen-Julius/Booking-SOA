from nameko.rpc import rpc
import dependencies as dependencies

class ReviewService:

    name = 'review_service'
    
    database = dependencies.Database()

    @rpc
    def add_review(self, booking_id, rating, comment, option_ids):
        response = self.database.add_review(booking_id=booking_id, rating=rating, comment=comment, option_ids=option_ids)
        return response
    
    @rpc
    def get_rating_type(self,service_type):
        response = self.database.get_rating_type(service_type=service_type)
        return response
    @rpc
    def get_information_provider(self,provider_name):
        response = self.database.get_information_provider(provider_name=provider_name)
        return response 
    @rpc
    def get_rating_provider(self,provider_name):
        response = self.database.get_rating_provider(provider_name=provider_name)
        return response

    @rpc
    def get_completed_booking(self, booking_type):
        response = self.database.get_completed_booking(booking_type=booking_type)
        return response
    @rpc
    def get_review_comment(self, provider_name):
        response = self.database.get_review_comment(provider_name=provider_name)
        return response
    @rpc
    def get_review_date(self, booking_id, booking_type):
        response = self.database.get_review_date(booking_id=booking_id,booking_type=booking_type)
        return response