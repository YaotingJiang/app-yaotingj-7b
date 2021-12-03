from models.rating import Rating

def init_ratings():
    existing_ratings = Rating.objects()
    if len(existing_ratings) == 0:
        create_rating('5', 'TEST DOGWALKER')


def get_rating(rating_id: str):
    if rating_id is None:
        rating_doc = Rating.objects()
    else:
        rating_doc = Rating.objects(id=rating_id)
    return rating_doc

def create_rating(score: int, dog_walker: str):
    rating_doc = Rating(score=score, dog_walker=dog_walker)
    rating_doc.save()
    return rating_doc

def update_rating(rating_id: str, score: int, dog_walker: str):
    rating_doc = Rating.objects(id=rating_id).first()  # extracting the first object from a list of one object
    rating_doc.update(score=score, dog_walker=dog_walker)
    rating_doc.reload()
    return rating_doc

def delete_rating(rating_id: str):
    rating_doc = Rating.objects(id=rating_id)
    rating_doc.delete()
    return rating_doc