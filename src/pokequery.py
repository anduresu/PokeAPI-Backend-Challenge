import json
import re
import requests

CONFIG_FILE = 'config.json'

with open(CONFIG_FILE, 'r') as f:
    config = json.load(f)

API_URL = config['API_URL']


def save_json(filename, data):
    """
    Saves a JSON file data into filename.
    :param filename: filename with json extension.
    :param data: JSON format dictionary.
    """

    with open(filename, 'w') as f:
        json.dump(data, f)


def update_limit():
    """
    Updates the maximum amount of Pokemons in the config file.
    """
    query_string = f'{API_URL}/pokemon/?'
    r = requests.get(query_string)
    config['POKEMON_LIMIT'] = int(r.json()['count'])
    save_json(CONFIG_FILE, config)


def query_names(limit):
    """
    Requests all Pokemon names to the API and converts the JSON answer to text.
    :param limit: maximum amount of Pokemon names to fetch
    :return: JSON answer as string
    """
    query_string = f'{API_URL}/pokemon/?limit={limit}'
    r = requests.get(query_string)
    text = json.dumps(r.json())
    return text


def count_matches(regex, text):
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


