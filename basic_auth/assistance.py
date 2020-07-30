import json


def get_config_data():
    with open("config.json", encoding='utf-8') as config_data:
        data = json.load(config_data)
    return data


def get_test_data():
    with open("test_data.json", encoding='utf-8') as config_data:
        data = json.load(config_data)
    return data
