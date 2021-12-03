from models.dogOwner import DogOwner


def get_dog(dog_owner_id: str):
    for dogOwner in DogOwner.objects:
        if str(dogOwner.id) == dog_owner_id:
            dog = {}
            dog['dog_name'] = dogOwner.dog_name
            dog['dog_size'] = dogOwner.dog_size
            dog['dog_sex'] = dogOwner.dog_sex
            return dog

def create_dog(dog_owner_id: str, dog_name: str, dog_size: str, dog_sex: str):
    for dogOwner in DogOwner.objects:
        if(dog_owner_id == str(dogOwner.id)):
            dogOwner.dog_name = dog_name
            dogOwner.dog_size = dog_size
            dogOwner.dog_sex = dog_sex
            dogOwner.save()
            return dogOwner

def update_dog(dog_owner_id: str, dog_name: str, dog_size: str, dog_sex: str):
    for dogOwner in DogOwner.objects:
        if(dog_owner_id == str(dogOwner.id)):
            dogOwner.dog_name = dog_name
            dogOwner.dog_size = dog_size
            dogOwner.dog_sex = dog_sex
            dogOwner.save()
            return dogOwner