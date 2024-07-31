import unittest
from src.services.pet_service import get_pets_by_name_and_category, place_order


class TestCheckAvailablePets(unittest.TestCase):

    def test_find_available_pets_and_place_order(self):
        pets = get_pets_by_name_and_category('pupo', 'pajaro')
        self.assertGreater(len(pets), 0)

        pet = pets[0]
        order = {
            'id': 0,
            'petId': pet['id'],
            'quantity': 1,
            'shipDate': '2023-12-01T00:00:00.000Z',
            'status': 'placed',
            'complete': True
        }
        placed_order = place_order(order)
        self.assertEqual(placed_order['petId'], pet['id'])
        self.assertEqual(placed_order['status'], 'placed')


if __name__ == '__main__':
    unittest.main()
