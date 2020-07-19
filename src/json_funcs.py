import json


def write_json(squares, FILE='json_data.json'):
    with open(FILE, 'w') as json_file:
        json.dump(squares, json_file)


def obtain_json(FILE='json_data.json'):
    try:
        with open(FILE, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        return {}
