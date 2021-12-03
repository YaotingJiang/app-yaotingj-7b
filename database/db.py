from flask_mongoengine import MongoEngine
from services.dogWalkerService import init_dog_walkers
from services.dogOwnerService import init_dog_owners
from services.routeService import init_routes
from services.paymentMethodService import init_payment_method
from services.ratingService import init_ratings

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)
    init_dog_walkers()
    init_dog_owners()
    init_routes()
    init_payment_method()
    init_ratings()

def fetch_engine():
    return db
