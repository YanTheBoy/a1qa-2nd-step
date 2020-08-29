import json
from string import ascii_uppercase, ascii_lowercase, digits
from random import choice
import os

TEST_DATA = "test_data.json"
CONFIG_SETUP = "config.json"



def get_config_data():
    with open(os.path.join("../testcases/", f"{CONFIG_SETUP}"), encoding='utf-8') as config_data:
        data = json.load(config_data)
    return data


def get_test_data():
    with open(os.path.join("../testcases/", f"{TEST_DATA}"), encoding='utf-8') as config_data:
        data = json.load(config_data)
    return data


def sort_list_by_user_id(post):
    return post['id']


def generate_string():
    return ''.join(choice(ascii_uppercase + ascii_lowercase + digits) for i in range(16))
