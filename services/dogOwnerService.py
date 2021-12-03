from models.dogOwner import DogOwner


# first_name = StringField(max_length=100, required=True)
# last_name = StringField(max_length=100, required=True)
# email = StringField(max_length=500, required=True)
# phone = StringField(max_length=10, required=True)
#
# street_address = StringField()
# city = StringField()
# state = StringField()
# zipcode = StringField()
# country = StringField()
# credit_card_num = StringField()
# expiration = StringField()
# security_code = StringField()
# dog_name = StringField()
# dog_size = StringField()
# dog_sex = StringField()

def init_dog_owners():
    existing_dog_owners = DogOwner.objects()
    if len(existing_dog_owners) == 0:
        create_dog_owner('dog', 'owner1', 'dogowner1@test.com', '4807773333', '111 toyama dr', 'Sunnyvale',
                         'CA', '94089', 'USA', '4400 3333 0000 1111', '11/11/25', '000', 'coco', 'small', 'female')


def create_dog_owner(first_name: str, last_name: str, email: str, phone: str, street_address: str, city: str, state: str, zipcode: str,
                     country: str, credit_card_num: str, expiration: str, security_code: str, dog_name: str, dog_size: str,
                     dog_sex: str):
    dog_owner_doc = DogOwner(first_name=first_name,
                             last_name=last_name,
                             email=email,
                             phone=phone,
                             street_address=street_address,
                             city=city,
                             state=state,
                             zipcode=zipcode,
                             country=country,
                             credit_card_num=credit_card_num,
                             expiration=expiration,
                             security_code=security_code,
                             dog_name=dog_name,
                             dog_size=dog_size,
                             dog_sex=dog_sex)
    dog_owner_doc.save()
    return dog_owner_doc

def get_dog_owner(dog_owner_id: str):
    if dog_owner_id is None:
        dog_owner_doc = DogOwner.objects()
    else:
        dog_owner_doc = DogOwner.objects(id=dog_owner_id)
    return dog_owner_doc


def update_dog_owner(dog_owner_id: str, email: str, phone: str):
    dog_owner_doc = DogOwner.objects(id=dog_owner_id).first()  # extracting the first object from a list of one object
    dog_owner_doc.update(email=email, phone=phone)
    dog_owner_doc.reload()
    return dog_owner_doc

def delete_dog_owner(dog_owner_id: str):
    dog_owner_doc = DogOwner.objects(id=dog_owner_id)
    dog_owner_doc.delete()
    return dog_owner_doc