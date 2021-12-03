from flask_restful import reqparse, Resource
from flask import make_response
from services.dogOwnerPaymentService import *

# credit_card_num = StringField()
# expiration = StringField()
# security_code = StringField()

post_parser = reqparse.RequestParser()
post_parser.add_argument('credit_card_num', type=str)
post_parser.add_argument('expiration', type=str)
post_parser.add_argument('security_code', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('credit_card_num', type=str)
patch_parser.add_argument('expiration', type=str)
patch_parser.add_argument('security_code', type=str)

headers = {'Content-Type': 'application/json'}
# sub-resources
class DogOwnerPaymentSubResource(Resource):
    def get(self, dog_owner_id):
        res = get_payment_method(dog_owner_id)
        print('res', res)
        return make_response(res, 200, headers)

    def post(self, dog_owner_id: str):
        if dog_owner_id is not None:
            args = post_parser.parse_args()
            print('args', args)
            res = create_payment_method(dog_owner_id, args.credit_card_num, args.expiration, args.security_code)
            return make_response(res.to_json(), 200, headers)
        return 400

    def patch(self, dog_owner_id: str):
        if dog_owner_id is not None:
            args = patch_parser.parse_args()
            res = update_payment_method(dog_owner_id, args.credit_card_num, args.expiration, args.security_code)
            return make_response(res.to_json(), 200, headers)
        return 400