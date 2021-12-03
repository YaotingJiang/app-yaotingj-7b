from flask import Flask
from flask_restful import Api
from resources.dogWalkerResources import DogWalkerResource
from resources.dogOwnerResources import DogOwnerResource
from resources.dogOwnerDogSubResources import DogOwnerDogSubResource
from resources.dogOwnerPaymentSubResources import DogOwnerPaymentSubResource
from resources.dogOwnerAddressSubResources import DogOwnerAddressSubResource
from resources.routeResources import RouteResource
from resources.paymentMethodResources import PaymentMethodResource
from resources.ratingResources import RatingResource
from database.db import initialize_db
from utils.JSONEncoder import MongoEngineJSONEncoder


app = Flask(__name__)  # Creating a FLASK app
app.config['MONGODB_SETTINGS'] = {
    'db': 'app-yaotingj-7b',
    'host': 'mongodb://localhost:27017/app-yaotingj-7b'
}

initialize_db(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)

api.add_resource(DogWalkerResource,
                 '/dog_walker',
                 '/dog_walker/',
                 '/dog_walker/<string:dog_walker_id>')

api.add_resource(DogOwnerResource,
                 '/dog_owner',
                 '/dog_owner/',
                 '/dog_owner/<string:dog_owner_id>')

api.add_resource(DogOwnerDogSubResource,
                 '/dog_owner/<string:dog_owner_id>/',
                 '/dog_owner/<string:dog_owner_id>/dog')

api.add_resource(DogOwnerPaymentSubResource,
                 '/dog_owner/<string:dog_owner_id>/',
                 '/dog_owner/<string:dog_owner_id>/payment')

api.add_resource(DogOwnerAddressSubResource,
                 '/dog_owner/<string:dog_owner_id>/',
                 '/dog_owner/<string:dog_owner_id>/address')


api.add_resource(RouteResource,
                 '/route',
                 '/route/',
                 '/route/<string:route_id>')



api.add_resource(PaymentMethodResource,
                 '/payment_method',
                 '/payment_method/',
                 '/payment_method/<string:payment_method_id>')


api.add_resource(RatingResource,
                 '/rating',
                 '/rating/',
                 '/rating/<string:rating_id>')

@app.route('/')
def entry():
    return "APP 7B"

if __name__ == "__main__":
    app.run()