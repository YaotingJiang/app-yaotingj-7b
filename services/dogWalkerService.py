from models.dogWalker import DogWalker


def init_dog_walkers():
    existing_dog_walkers = DogWalker.objects()
    if len(existing_dog_walkers) == 0:
        create_dog_walker('test', '1', 'dg1@test.com', '6178889999')


def get_dog_walker(dog_walker_id: str):
    if dog_walker_id is None:
        dog_walker_doc = DogWalker.objects()
    else:
        dog_walker_doc = DogWalker.objects(id=dog_walker_id)
    return dog_walker_doc

def create_dog_walker(first_name: str, last_name: str, email: str, phone: str, rating: int = 0):
    dog_walker_doc = DogWalker(first_name=first_name,
                               last_name=last_name,
                               email=email,
                               phone=phone,
                               rating=rating)
    dog_walker_doc.save()
    return dog_walker_doc

def update_dog_walker(dog_walker_id: str, email: str, phone: str, rating: int = 0):
    dog_walker_doc = DogWalker.objects(id=dog_walker_id).first()  # extracting the first object from a list of one object
    dog_walker_doc.update(email=email, phone=phone, rating=rating)
    dog_walker_doc.reload()
    return dog_walker_doc

def delete_dog_walker(dog_walker_id: str):
    dog_walker_doc = DogWalker.objects(id=dog_walker_id)
    dog_walker_doc.delete()
    return dog_walker_doc