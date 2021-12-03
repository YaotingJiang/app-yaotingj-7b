from flask_restful import reqparse, Resource
from flask import make_response
from services.dogOwnerDogService import *



post_parser = reqparse.RequestParser()
post_parser.add_argument('dog_name', type=str)
post_parser.add_argument('dog_size', type=str)
post_parser.add_argument('dog_sex', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('dog_name', type=str)
patch_parser.add_argument('dog_size', type=str)
patch_parser.add_argument('dog_sex', type=str)

headers = {'Content-Type': 'application/json'}
# sub-resources
class DogOwnerDogSubResource(Resource):
    def get(self, dog_owner_id):
        res = get_dog(dog_owner_id)
        print('res', res)
        return make_response(res, 200, headers)

    def post(self, dog_owner_id: str):
        if dog_owner_id is not None:
            args = post_parser.parse_args()
            print('args', args)
            res = create_dog(dog_owner_id, args.dog_name, args.dog_size, args.dog_sex)
            return make_response(res.to_json(), 200, headers)
        return 400

    def patch(self, dog_owner_id: str):
        if dog_owner_id is not None:
            args = patch_parser.parse_args()
            res = update_dog(dog_owner_id, args.dog_name, args.dog_size, args.dog_sex)
            return make_response(res.to_json(), 200, headers)
        return 400