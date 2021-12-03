from flask_restful import reqparse, Resource
from flask import make_response
from services.ratingService import *

# street_address = StringField(required=True)
# state = StringField(required=True)
# zipcode = StringField(max_length=5, required=True)

post_parser = reqparse.RequestParser()
post_parser.add_argument('score', type=str)
post_parser.add_argument('dog_walker', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('score', type=str)
patch_parser.add_argument('dog_walker', type=str)

headers = {'Content-Type': 'application/json'}

class RatingResource(Resource):
    def get(self, rating_id=None):
        res = get_rating(rating_id)
        return make_response(res.to_json(), 200, headers)

    def post(self):
        args = post_parser.parse_args()
        res = create_rating(args.score, args.dog_walker)
        return make_response(res.to_json(), 200, headers)

    def patch(self, rating_id=None):
        if rating_id is not None:
            args = patch_parser.parse_args()
            res = update_rating(rating_id, args.score, args.dog_walker)
            return make_response(res.to_json(), 200, headers)
        return 400

    def delete(self, rating_id=None):
        if rating_id is not None:
            res = delete_rating(rating_id)
            return make_response(res.to_json(), 200, headers)
        return 400