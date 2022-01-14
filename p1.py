from src.pokequery import query_names
from src.pokequery import count_matches

import json

CONFIG_FILE = 'config.json'

with open(CONFIG_FILE, 'r') as f:
    config = json.load(f)

API_URL = config['API_URL']
REGEX = config['REGEX']
POKEMON_LIMIT = config['POKEMON_LIMIT']

def pokemon_names_matches():
    """
    :return: the number of Pokemon names with "at" and two occurrences of "a".
    """
    text = query_names(POKEMON_LIMIT)
    num_matches = count_matches(REGEX, text)
    return num_matches

if __name__ == "__main__":
    print(pokemon_names_matches())