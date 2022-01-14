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
