from models.dogOwner import DogOwner

def get_payment_method(dog_owner_id: str):
    for dogOwner in DogOwner.objects:
        if str(dogOwner.id) == dog_owner_id:
            payment_method = {}
            payment_method['credit_card_num'] = dogOwner.credit_card_num
            payment_method['expiration'] = dogOwner.expiration
            payment_method['security_code'] = dogOwner.security_code
            return payment_method

def create_payment_method(dog_owner_id: str, credit_card_num: str, expiration: str, security_code: str):
    for dogOwner in DogOwner.objects:
        if(dog_owner_id == str(dogOwner.id)):
            dogOwner.credit_card_num = credit_card_num
            dogOwner.expiration = expiration
            dogOwner.security_code = security_code
            dogOwner.save()
            return dogOwner

def update_payment_method(dog_owner_id: str, credit_card_num: str, expiration: str, security_code: str):
    for dogOwner in DogOwner.objects:
        if(dog_owner_id == str(dogOwner.id)):
            dogOwner.credit_card_num = credit_card_num
            dogOwner.expiration = expiration
            dogOwner.security_code = security_code
            dogOwner.save()
            return dogOwner