from marshmallow import Schema, fields, validate


class BookingSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    booking_type = fields.Str(required=True)
    booking_date = fields.DateTime(required=True)
    status = fields.Int(required=True)
    total_price = fields.Decimal(places=2, required=True)
    asuransi_id = fields.Int(allow_none=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class BookingAirlinesSchema(Schema):
    id = fields.Int(dump_only=True)
    booking_id = fields.Int(required=True)
    flight_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class BookingAttractionsSchema(Schema):
    id = fields.Int(dump_only=True)
    booking_id = fields.Int(required=True)
    attraction_provider_name = fields.Str(required=True)
    paket_attraction_id = fields.Int(required=True)
    visit_date = fields.Date(required=True)
    number_of_tickets = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class BookingHotelsSchema(Schema):
    id = fields.Int(dump_only=True)
    booking_id = fields.Int(required=True)
    hotel_name = fields.Str(required=True)
    room_type = fields.Int(required=True)
    check_in_date = fields.Date(required=True)
    check_out_date = fields.Date(required=True)
    number_of_rooms = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class BookingRentalsSchema(Schema):
    id = fields.Int(dump_only=True)
    booking_id = fields.Int(required=True)
    rental_provider_name = fields.Str(required=True)
    car_id = fields.Int(required=True)
    pickup_date = fields.DateTime(required=True)
    return_date = fields.DateTime(required=True)
    pickup_location = fields.Str(required=True)
    return_location = fields.Str(required=True)
    is_with_driver = fields.Bool(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    booking_id = fields.Int(required=True)
    rating = fields.Int(required=True, validate=validate.Range(min=1, max=5))
    comment = fields.Str(allow_none=True)
    is_edited = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class ReviewRentalSchema(Schema):
    id = fields.Int(dump_only=True)
    review_id = fields.Int(required=True)
    provider_name = fields.Str(required=True)
    category = fields.Str(validate=validate.OneOf(['Car Cleanliness', 'Simple Pick-up And Drop-off Process', 'Staff is Helpful']))
    count = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class ReviewHotelSchema(Schema):
    id = fields.Int(dump_only=True)
    review_id = fields.Int(required=True)
    provider_name = fields.Str(required=True)
    category = fields.Str(validate=validate.OneOf(['Strategic Location', 'Great Accomodation', 'Staff is Friendly']))
    count = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class ReviewAirlineSchema(Schema):
    id = fields.Int(dump_only=True)
    review_id = fields.Int(required=True)
    provider_name = fields.Str(required=True)
    category = fields.Str(validate=validate.OneOf(['Car Cleanliness', 'Simple Pick-up And Drop-off Process', 'Staff is Helpful']))
    count = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class ReviewAttractionSchema(Schema):
    id = fields.Int(dump_only=True)
    review_id = fields.Int(required=True)
    provider_name = fields.Str(required=True)
    category = fields.Str(validate=validate.OneOf(['Car Cleanliness', 'Simple Pick-up And Drop-off Process', 'Staff is Helpful']))
    count = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)