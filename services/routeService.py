from models.route import Route

def init_routes():
    existing_routes = Route.objects()
    if len(existing_routes) == 0:
        create_route('400 Toyama Dr', 'california', '94089')


def get_route(route_id: str):
    if route_id is None:
        route_doc = Route.objects()
    else:
        route_doc = Route.objects(id=route_id)
    return route_doc

def create_route(address: str, state: str, zipcode: str):
    route_doc = Route(street_address=address, state=state, zipcode=zipcode)
    route_doc.save()
    return route_doc

def update_route(route_id: str, state: str, zipcode: str, address: str):
    route_doc = Route.objects(id=route_id).first()  # extracting the first object from a list of one object
    route_doc.update(street_address=address, state=state, zipcode=zipcode)
    route_doc.reload()
    return route_doc

def delete_route(route_id: str):
    route_doc = Route.objects(id=route_id)
    route_doc.delete()
    return route_doc