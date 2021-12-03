from flask_restful import reqparse, Resource
from flask import make_response
from services.routeService import *

# street_address = StringField(required=True)
# state = StringField(required=True)
# zipcode = StringField(max_length=5, required=True)

post_parser = reqparse.RequestParser()
post_parser.add_argument('street_address', type=str)
post_parser.add_argument('state', type=str)
post_parser.add_argument('zipcode', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('street_address', type=str)
patch_parser.add_argument('state', type=str)
patch_parser.add_argument('zipcode', type=str)

headers = {'Content-Type': 'application/json'}

class RouteResource(Resource):
    def get(self, route_id=None):
        res = get_route(route_id)
        return make_response(res.to_json(), 200, headers)

    def post(self):
        args = post_parser.parse_args()
        res = create_route(args.street_address, args.state, args.zipcode)
        return make_response(res.to_json(), 200, headers)

    def patch(self, route_id=None):
        if route_id is not None:
            args = patch_parser.parse_args()
            res = update_route(route_id, args.street_address, args.state, args.zipcode)
            return make_response(res.to_json(), 200, headers)
        return 400

    def delete(self, route_id=None):
        if route_id is not None:
            res = delete_route(route_id)
            return make_response(res.to_json(), 200, headers)
        return 400