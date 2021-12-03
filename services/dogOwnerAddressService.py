from models.dogOwner import DogOwner

# street_address = StringField()
# city = StringField()
# state = StringField()
# zipcode = StringField()
# country = StringField()

def get_address(dog_owner_id: str):
    for dogOwner in DogOwner.objects:
        if str(dogOwner.id) == dog_owner_id:
            address = {}
            address['street_address'] = dogOwner.street_address
            address['city'] = dogOwner.city
            address['state'] = dogOwner.state
            address['zipcode'] = dogOwner.zipcode
            address['country'] = dogOwner.country
            return address

def create_address(dog_owner_id: str, street_address: str, city: str, state: str, zipcode: str, country: str):
    for dogOwner in DogOwner.objects:
        if(dog_owner_id == str(dogOwner.id)):
            dogOwner.street_address = street_address
            dogOwner.city = city
            dogOwner.state = state
            dogOwner.zipcode = zipcode
            dogOwner.country = country
            dogOwner.save()
            return dogOwner

def update_address(dog_owner_id: str, street_address: str, city: str, state: str, zipcode: str, country: str):
    for dogOwner in DogOwner.objects:
        if(dog_owner_id == str(dogOwner.id)):
            dogOwner.street_address = street_address
            dogOwner.city = city
            dogOwner.state = state
            dogOwner.zipcode = zipcode
            dogOwner.country = country
            dogOwner.save()
            return dogOwner