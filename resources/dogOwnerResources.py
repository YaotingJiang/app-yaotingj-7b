from flask_restful import reqparse, Resource
from flask import make_response
from services.dogOwnerService import *

post_parser = reqparse.RequestParser()
post_parser.add_argument('first_name', type=str)
post_parser.add_argument('last_name', type=str)
post_parser.add_argument('email', type=str)
post_parser.add_argument('phone', type=str)

post_parser.add_argument('street_address', type=str)
post_parser.add_argument('city', type=str)
post_parser.add_argument('state', type=str)
post_parser.add_argument('country', type=str)

post_parser.add_argument('credit_card_num', type=str)
post_parser.add_argument('expiration', type=str)
post_parser.add_argument('security_code', type=str)

post_parser.add_argument('dog_name', type=str)
post_parser.add_argument('dog_size', type=str)
post_parser.add_argument('dog_sex', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('email', type=str)
patch_parser.add_argument('phone', type=str)
patch_parser.add_argument('rating', type=int)

headers = {'Content-Type': 'application/json'}

class DogOwnerResource(Resource):

    # resources
    def get(self, dog_owner_id=None):
        if dog_owner_id is None:
            args = reqparse.request.args;
            query_from = int(args['from']) if 'from' in args else 0
            query_count = int(args['count']) if 'count' in args else 50
            query_sorting_by_lastname = int(args['rating']) if 'rating' in args else 0
            res = get_dog_owner(query_from, query_count, query_sorting_by_lastname)
        else:
            res = get_dog_owner_by_id(dog_owner_id)
        return make_response(res.to_json(), 200, headers)

    def post(self):
        args = post_parser.parse_args()
        res = create_dog_owner(args.first_name, args.last_name, args.email, args.phone, args.street_address,
                               args.city, args.state, args.country, args.credit_card_num, args.expiration,
                               args.security_code, args.dog_name, args.dog_size, args.dog_sex)
        return make_response(res.to_json(), 200, headers)

    def patch(self, dog_owner_id=None):
        if dog_owner_id is not None:
            args = patch_parser.parse_args()
            res = update_dog_owner(dog_owner_id, args.email, args.phone)
            return make_response(res.to_json(), 200, headers)
        return 400

    def delete(self, dog_owner_id=None):
        if dog_owner_id is not None:
            res = delete_dog_owner(dog_owner_id)
            return make_response(res.to_json(), 200, headers)
        return 400