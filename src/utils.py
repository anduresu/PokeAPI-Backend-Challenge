import json
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

