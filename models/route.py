from mongoengine import Document, StringField, IntField


class Route(Document):
    street_address = StringField(required=True)
    state = StringField(required=True)
    zipcode = StringField(max_length=5, required=True)