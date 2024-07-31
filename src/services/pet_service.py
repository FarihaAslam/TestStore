import requests

BASE_URL = 'https://petstore.swagger.io/v2'


def get_pets_by_name_and_category(name, category):
    response = requests.get(f'{BASE_URL}/pet/findByStatus', params={'status': 'available'})
    pets = response.json()
    return [pet for pet in pets if pet['name'] == name and pet['category']['name'] == category]


def place_order(order):
    response = requests.post(f'{BASE_URL}/store/order', json=order)
    return response.json()


def update_pet_tags(pet_id, tags):
    response = requests.post(f'{BASE_URL}/pet/{pet_id}', data={'tags': tags})
    return response.json()
