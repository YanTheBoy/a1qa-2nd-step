import json
from string import ascii_uppercase, ascii_lowercase, digits
from random import choice


def get_config_data():
    with open("config.json", encoding='utf-8') as config_data:
        data = json.load(config_data)
    return data


def get_test_data():
    with open("test_data.json", encoding='utf-8') as config_data:
        data = json.load(config_data)
    return data


def sort_list_by_user_id(post):
    return post['id']


def generate_string():
    return ''.join(choice(ascii_uppercase + ascii_lowercase + digits) for i in range(16))
