import json
import re
import requests

CONFIG_FILE = 'config.json'

with open(CONFIG_FILE, 'r') as f:
    config = json.load(f)

API_URL = config['API_URL']

def query_pokemon_names(limit):
    """
    Requests all Pokemon names to the API and converts the JSON answer to text.
    :param limit: maximum amount of Pokemon names to fetch
    :return: JSON answer as string
    """
    query_string = f'{API_URL}/pokemon/?limit={limit}'
    r = requests.get(query_string)
    return r.json()


def count_matches(regex, data):
    text = json.dumps(data)
    return int(len(re.findall(regex, text)))


def length_egg_groups(egg_groups):
    """
    Creates a set with the Pokemon names from the egg groups and returns its length.
    :param egg_groups: a list of egg group names.
    :return: the number of Pokemons in all egg groups.
    """
    species = set()
    for eg in egg_groups:
        query_string = f'{API_URL}/egg-group/{eg}'
        r = requests.get(query_string)
        data = r.json()['pokemon_species']
        for d in data:
            species.add(d['name'])
    return len(species)

def count_shared_egg_group_species(name):
    """
    Counts the number of Pokemons with the same egg group as "name".
    :param name: the name of a Pokemon
    :return: the number of Pokemons with the same egg group.
    """
    query_string = f'{API_URL}/pokemon-species/{name}'
    r = requests.get(query_string)
    data = r.json()
    egg_groups = [d['name'] for d in data['egg_groups']]
    return length_egg_groups(egg_groups)


def pokemon_id_from_url(url):
    return int(re.search(r'\/(\d+)\/', url)[1])


def query_pokemon_type_on_interval(pokemon_type, interval):
    """
    Obtains a list of names with Pokemons under interval from the given type.
    :param pokemon_type: a pokemon type
    :param interval: an array with two values [min_value, max_value]
    :return: a list of Pokemon names
    """
    min_id, max_id = interval
    query_string = f'{API_URL}/type/{pokemon_type}'
    r = requests.get(query_string)
    data = r.json()['pokemon']
    pokemon_names = []
    for d in data:
        pokemon_id = pokemon_id_from_url(d['pokemon']['url'])
        if (pokemon_id >= min_id) and (pokemon_id <= max_id):
            pokemon_names.append(d['pokemon']['name'])
    return pokemon_names


def query_weight(name):
    query_string = f'{API_URL}/pokemon/{name}'
    r = requests.get(query_string)
    weight = int(r.json()['weight'])
    return weight