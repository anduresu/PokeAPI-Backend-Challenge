import json
import sys

from src.pokequery import query_pokemon_type_on_interval
from src.pokequery import query_weight

CONFIG_FILE = 'config.json'

with open(CONFIG_FILE, 'r') as f:
    config = json.load(f)

GENERATION_INTERVAL = config['GENERATION_INTERVAL']
POKEMON_TYPE = config['POKEMON_TYPE']

def get_min_max_weight_by_type(pokemon_type):
    """
    Obtains the maximum and minimum weight of Pokemons of a type
    :param pokemon_type: the pokemon type
    :return: a list of [min_weight, max_weight]
    """
    type_list = query_pokemon_type_on_interval(pokemon_type, GENERATION_INTERVAL)
    min_weight = sys.maxsize
    max_weight = 0
    for pokemon in type_list:
        weight = query_weight(pokemon)
        min_weight = min_weight if min_weight < weight else weight
        max_weight = max_weight if max_weight > weight else weight
    return [max_weight, min_weight]

if __name__ == '__main__':
    print(get_min_max_weight_by_type(POKEMON_TYPE))
