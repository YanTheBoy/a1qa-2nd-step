from framework.utils.assistance import get_config_data, get_test_data
import requests
test_data = get_test_data()
config_data = get_config_data()

URL = config_data['url']
POSTS = test_data['posts']
USERS = test_data['users']


def get_status_code(response):
    return response.status_code

def get_users(*args):
    url = URL + USERS
    for path in args:
        url = url+path
    return requests.get(url)

def get_posts(*args):
    url = URL + POSTS
    for path in args:
        url = url+path
    return requests.get(url)


def send_post_request(url, *args, data):
    for path in args:
        url = url+path
    return requests.post(url, data)
