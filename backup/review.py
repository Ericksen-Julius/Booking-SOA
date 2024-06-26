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
    # @rpc
    # def get_reviews_by_booking(self, booking_id):
    #     reviews = self.database.get_reviews_by_booking(booking_id)
    #     return reviews

    # @rpc
    # def get_reviews_by_user(self, user_id):
    #     reviews = self.database.get_reviews_by_user(user_id)
    #     return reviews

    # @rpc
    # def edit_review(self, review_id, rating, review_text):
    #     response = self.database.edit_review(review_id, rating, review_text)
    #     if response:
    #         self.database.set_review_as_edited(review_id)
    #     return response
    
    # @rpc
    # def get_reviews_by_service_type(self, service_type):
    #     reviews = self.database.get_reviews_by_service_type(service_type)
    #     return reviews

    # @rpc
    # def get_average_rating_by_service_type(self, service_type):
    #     average_rating = self.database.get_average_rating_by_service_type(service_type)
    #     return average_rating

    # @rpc
    # def get_reviews_and_average_by_service_type(self, service_type):
    #     reviews = self.get_reviews_by_service_type(service_type)
    #     average_rating = self.get_average_rating_by_service_type(service_type)
    #     return {
    #         "reviews": reviews,
    #         "average_rating": average_rating
    #     }