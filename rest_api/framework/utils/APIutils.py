import requests


def get_status_code(response):
    return response.status_code


def send_get_request(url, *args):
    for path in args:
        url = url+path
    return requests.get(url)


def send_post_request(url, *args, data):
    for path in args:
        url = url+path
    return requests.post(url, data)
