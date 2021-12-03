from flask_restful import reqparse, Resource
from flask import make_response
from services.dogWalkerService import *

post_parser = reqparse.RequestParser()
post_parser.add_argument('first_name', type=str)
post_parser.add_argument('last_name', type=str)
post_parser.add_argument('email', type=str)
post_parser.add_argument('phone', type=str)
post_parser.add_argument('rating', type=int, default=0)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('email', type=str)
patch_parser.add_argument('phone', type=str)
patch_parser.add_argument('rating', type=int)

headers = {'Content-Type': 'application/json'}

class DogWalkerResource(Resource):
    def get(self, dog_walker_id=None):
        res = get_dog_walker(dog_walker_id)
        return make_response(res.to_json(), 200, headers)

    def post(self):
        args = post_parser.parse_args()
        res = create_dog_walker(args.first_name, args.last_name, args.email, args.phone, args.rating)
        return make_response(res.to_json(), 200, headers)

    def patch(self, dog_walker_id=None):
        if dog_walker_id is not None:
            args = patch_parser.parse_args()
            res = update_dog_walker(dog_walker_id, args.email, args.phone, args.rating)
            return make_response(res.to_json(), 200, headers)
        return 400

    def delete(self, dog_walker_id=None):
        if dog_walker_id is not None:
            res = delete_dog_walker(dog_walker_id)
            return make_response(res.to_json(), 200, headers)
        return 400