from flask_restful import reqparse, Resource
from flask import make_response
from services.paymentMethodService import *

# Credit card number
# Expiration date
# Security code
# billing address

post_parser = reqparse.RequestParser()
post_parser.add_argument('credit_card', type=str)
post_parser.add_argument('expiration_date', type=str)
post_parser.add_argument('security_code', type=str)
post_parser.add_argument('billing_address', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('credit_card', type=str)
patch_parser.add_argument('expiration_date', type=str)
patch_parser.add_argument('security_code', type=str)
patch_parser.add_argument('billing_address', type=str)

headers = {'Content-Type': 'application/json'}

class PaymentMethodResource(Resource):
    def get(self, payment_method_id=None):
        res = get_payment_method(payment_method_id)
        return make_response(res.to_json(), 200, headers)

    def post(self):
        args = post_parser.parse_args()
        res = create_payment_method(args.credit_card, args.expiration_date, args.security_code, args.billing_address)
        return make_response(res.to_json(), 200, headers)

    def patch(self, payment_method_id=None):
        if payment_method_id is not None:
            args = patch_parser.parse_args()
            res = update_payment_method(payment_method_id, args.credit_card, args.expiration_date, args.security_code, args.billing_address)
            return make_response(res.to_json(), 200, headers)
        return 400

    def delete(self, payment_method_id=None):
        if payment_method_id is not None:
            res = delete_payment_method(payment_method_id)
            return make_response(res.to_json(), 200, headers)
        return 400