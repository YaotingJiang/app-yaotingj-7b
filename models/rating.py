from mongoengine import Document, StringField, IntField


class Rating(Document):
    score = IntField(required=True)
    dog_walker = StringField(required=True)