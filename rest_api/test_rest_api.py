from logger import appLogger
from APIutils import send_get_request, get_status_code, send_post_request
from assistance import get_config_data, get_test_data, generate_string, sort_list_by_user_id

test_data = get_test_data()
config_data = get_config_data()
RESPONSE_200 = int(test_data['response_200'])
RESPONSE_201 = int(test_data['response_201'])
RESPONSE_404 = int(test_data['response_404'])


def test_rest_api():
    appLogger.debug('Make a GET request to', config_data['url'], ' for all posts')
    response = send_get_request(config_data['url'], test_data['posts'])
    appLogger.debug('Assert response status code is 200')
    assert get_status_code(response) == RESPONSE_200, 'Status code is not 200'
    posts = response.json()
    appLogger.debug('Assert response is Json')
    assert posts, 'response is not in JSON'
    appLogger.debug('Assert json file sorted')
    assert posts == sorted(posts, key=sort_list_by_user_id), 'Posts list is not sorted'

    appLogger.debug('Send request for 99 post')
    response = send_get_request(
        config_data['url'],
        test_data['posts'],
        test_data['post_99']['id'])
    appLogger.debug('Assert response status code is 200')
    assert get_status_code(response) == RESPONSE_200, 'Status code is not 200'
    response_content = response.json()
    appLogger.debug('Assert content in userId and id')
    assert response_content['userId'] == int(test_data['post_99']['userId']) \
        and response_content['id'] == int(test_data['post_99']['id']), 'Wrong "Id"s in response was delivered'
    appLogger.debug('Assert fields are not empty')
    assert response_content['title'] and response_content['body'], 'Response "title" and "body" are empty'

    appLogger.debug('Send request for 150 post')
    response = send_get_request(
        config_data['url'],
        test_data['posts'],
        test_data['post_150'])
    appLogger.debug('Assert response status code is 404')
    assert get_status_code(response) == RESPONSE_404, 'Status code is not 404'

    appLogger.debug('Send POST request')
    data_to_post = {
        'userId': str(test_data['post_101']['userId']),
        'id': test_data['post_101']['id'],
        'title': generate_string(),
        'body': generate_string()}
    response = send_post_request(config_data['url'], test_data['posts'],
                                 data=data_to_post,
                                 )

    appLogger.debug('Assert response status code is 201')
    assert get_status_code(response) == RESPONSE_201, 'Status code is not 201'
    appLogger.debug('Assert response content equal to send data')
    assert response.json() == data_to_post, 'Response and posted data are not equal'

    appLogger.debug('Make GET request for users/')
    response = send_get_request(config_data['url'], test_data['users'], str(test_data['user_5']['id']))
    appLogger.debug('Assert response status code is 200')
    assert get_status_code(response) == RESPONSE_200, 'Status code is not 200'
    appLogger.debug('Assert response is Json')
    user_data = response.json()
    assert user_data, 'response is not in JSON'
    appLogger.debug('Assert collected data for user 5')
    assert user_data == test_data['user_5'], 'Users data are not equal'
