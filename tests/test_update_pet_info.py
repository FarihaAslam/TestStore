import unittest
from src.services.pet_service import get_pets_by_name_and_category, update_pet_tags


class TestUpdatePetInfo(unittest.TestCase):

    def test_update_pet_info(self):
        pets = get_pets_by_name_and_category('kurikuri', 'Pomeranian')
        self.assertGreater(len(pets), 0)

        pet = pets[0]
        updated_pet = update_pet_tags(pet['id'], [{'id': 1, 'name': 'Super Cute'}])
        tag_names = [tag['name'] for tag in updated_pet['tags']]
        self.assertIn('Super Cute', tag_names)


if __name__ == '__main__':
    unittest.main()
