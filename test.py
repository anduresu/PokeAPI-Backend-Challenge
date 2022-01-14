import json
import unittest

from src.pokequery import count_matches
from src.pokequery import length_egg_groups
from src.pokequery import count_shared_egg_group_species
from src.pokequery import query_pokemon_type_on_interval
from src.pokequery import query_weight

with open('test_sample.json','r') as f:
    DATA = json.load(f)



class TestFunctionalities(unittest.TestCase):

    def test_name_match(self):
        self.assertEqual(count_matches(r'name[^,]*charmander[^,]*', DATA), 1)
    def test_name_pattern_match(self):
        self.assertEqual(count_matches(r'name[^,]*saur[^,]*', DATA), 3)
    def test_name_repeated_letters(self):
        self.assertEqual(count_matches(r'name[^,]*u[^,]*u[^,]*', DATA), 2)
    def test_egg_group_simple(self):
        self.assertEqual(length_egg_groups(['ditto']), 1)
    def test_shared_egg_group_simple(self):
        self.assertEqual(count_shared_egg_group_species('ditto'), 1)
    def test_pokemon_type_null_interval(self):
        self.assertEqual(query_pokemon_type_on_interval('normal',[2000, 2001]), [])
    def test_pokemon_type_exact_interval(self):
        self.assertEqual(query_pokemon_type_on_interval('normal', [132, 132]), ['ditto'])
    def test_weight(self):
        self.assertEqual(query_weight("ditto"), 40)

if __name__ == '__main__':
    unittest.main()