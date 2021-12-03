from flask_restful import reqparse, Resource
from flask import make_response
from services.dogOwnerAddressService import *

# street_address = StringField()
# city = StringField()
# state = StringField()
# zipcode = StringField()
# country = StringField()

post_parser = reqparse.RequestParser()
post_parser.add_argument('street_address', type=str)
post_parser.add_argument('city', type=str)
post_parser.add_argument('state', type=str)
post_parser.add_argument('zipcode', type=str)
post_parser.add_argument('country', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('street_address', type=str)
patch_parser.add_argument('city', type=str)
patch_parser.add_argument('state', type=str)
patch_parser.add_argument('zipcode', type=str)
patch_parser.add_argument('country', type=str)

headers = {'Content-Type': 'application/json'}
# sub-resources
class DogOwnerAddressSubResource(Resource):
    def get(self, dog_owner_id):
        res = get_address(dog_owner_id)
        print('res', res)
        return make_response(res, 200, headers)

    def post(self, dog_owner_id: str):
        if dog_owner_id is not None:
            args = post_parser.parse_args()
            print('args', args)
            res = create_address(dog_owner_id, args.street_address, args.city, args.state, args.zipcode, args.country)
            return make_response(res.to_json(), 200, headers)
        return 400

    def patch(self, dog_owner_id: str):
        if dog_owner_id is not None:
            args = patch_parser.parse_args()
            res = update_address(dog_owner_id, args.street_address, args.city, args.state, args.zipcode, args.country)
            return make_response(res.to_json(), 200, headers)
        return 400