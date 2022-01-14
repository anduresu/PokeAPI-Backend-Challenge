import json
import unittest

from src.pokequery import count_matches
from src.pokequery import length_egg_groups
from src.pokequery import count_shared_egg_group_species

with open('test_sample.json','r') as f:
    TEST_TEXT = str(json.load(f))



class TestFunctionalities(unittest.TestCase):

    def test_name_match(self):
        self.assertEqual(count_matches(r'name[^,]*charmander[^,]*', TEST_TEXT), 1)
    def test_name_pattern_match(self):
        self.assertEqual(count_matches(r'name[^,]*saur[^,]*', TEST_TEXT), 3)
    def test_name_repeated_letters(self):
        self.assertEqual(count_matches(r'name[^,]*u[^,]*u[^,]*', TEST_TEXT), 2)
    def test_egg_group_simple(self):
        self.assertEqual(length_egg_groups(['ditto']), 1)
    def test_shared_egg_group_simple(self):
        self.assertEqual(count_shared_egg_group_species('ditto'), 1)

if __name__ == '__main__':
    unittest.main()