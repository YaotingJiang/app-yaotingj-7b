from mongoengine import Document, StringField, IntField


class DogWalker(Document):
    first_name = StringField(max_length=100, required=True)
    last_name = StringField(max_length=100, required=True)
    email = StringField(max_length=500, required=True)
    phone = StringField(max_length=10, required=True)
    rating = IntField(default=0)