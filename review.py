from nameko.rpc import rpc
import dependencies

class ReviewService:

    name = 'review_service'
    
    database = dependencies.Database()

    @rpc
    def add_review(self, booking_id, user_id, rating, review_text):
        response = self.database.add_review(booking_id, user_id, rating, review_text)
        return response

    @rpc
    def get_reviews_by_booking(self, booking_id):
        reviews = self.database.get_reviews_by_booking(booking_id)
        return reviews

    @rpc
    def get_reviews_by_user(self, user_id):
        reviews = self.database.get_reviews_by_user(user_id)
        return reviews

    @rpc
    def edit_review(self, review_id, rating, review_text):
        response = self.database.edit_review(review_id, rating, review_text)
        if response:
            self.database.set_review_as_edited(review_id)
        return response