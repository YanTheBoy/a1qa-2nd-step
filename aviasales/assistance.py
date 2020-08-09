import json
from string import ascii_uppercase, ascii_lowercase, digits
from random import choice
import datetime


def get_config_data():
    with open("config.json", encoding='utf-8') as config_data:
        data = json.load(config_data)
    return data


def get_test_data():
    with open("test_data.json", encoding='utf-8') as config_data:
        data = json.load(config_data)
    return data


def generate_string():
    return ''.join(choice(ascii_uppercase + ascii_lowercase + digits) for i in range(16))


def get_current_date():
    return datetime.datetime.now().strftime("%a %b %d %Y")


def get_random_number(row_lenght):
    return choice(range(row_lenght))
