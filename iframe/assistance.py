import json
from string import ascii_uppercase, ascii_lowercase, digits
from random import choice


def get_config_data():
    with open("config.json", encoding='utf-8') as config_data:
        data = json.load(config_data)
    return data

def get_testrail_data():
    with open("testrail.json", encoding='utf-8') as config_data:
        data = json.load(config_data)
    return data


def get_asserts_data():
    with open("asserts.json", encoding='utf-8') as config_data:
        data = json.load(config_data)
    return data


def generate_string():
    return ''.join(choice(ascii_uppercase + ascii_lowercase + digits) for i in range(16))