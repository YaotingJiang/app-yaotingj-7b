from mongoengine import Document, StringField

class DogOwner(Document):
    first_name = StringField(max_length=100, required=True)
    last_name = StringField(max_length=100, required=True)
    email = StringField(max_length=500, required=True)
    phone = StringField(max_length=10, required=True)

    street_address = StringField()
    city = StringField()
    state = StringField()
    zipcode = StringField()
    country = StringField()
    credit_card_num = StringField()
    expiration = StringField()
    security_code = StringField()
    dog_name = StringField()
    dog_size = StringField()
    dog_sex = StringField()