from framework.logger import appLogger
from framework.utils.APIutils import get_posts, get_users, get_status_code, send_post_request
from framework.utils.assistance import get_config_data, get_test_data, generate_string, sort_list_by_user_id
from http import HTTPStatus
test_data = get_test_data()
config_data = get_config_data()


def test_rest_api():
    appLogger.debug('Make a GET request to', config_data['url'], ' for all posts')
    response = get_posts()
    appLogger.debug('Assert response status code is 200')
    assert get_status_code(response) == HTTPStatus.OK, 'Expected HTTP status is 200'
    posts = response.json()
    appLogger.debug('Assert response is Json')
    assert posts, 'response is not in JSON'
    appLogger.debug('Assert json file sorted')
    assert posts == sorted(posts, key=sort_list_by_user_id), 'Posts list is not sorted'

    appLogger.debug('Send request for 99 post')
    response = get_posts(test_data['post_99']['id'])
    appLogger.debug('Assert response status code is 200')
    assert get_status_code(response) == HTTPStatus.OK, 'Expected HTTP status is 200'
    response_content = response.json()
    appLogger.debug('Assert content in userId and id')
    assert response_content['userId'] == int(test_data['post_99']['userId']) \
        and response_content['id'] == int(test_data['post_99']['id']), 'Wrong "Id"s in response was delivered'
    appLogger.debug('Assert fields are not empty')
    assert response_content['title'] and response_content['body'], 'Response "title" and "body" are empty'

    appLogger.debug('Send request for 150 post')
    response = get_posts(test_data['post_150'])
    appLogger.debug('Assert response status code is 404')
    assert get_status_code(response) == HTTPStatus.NOT_FOUND, 'Expected HTTP status is 404'

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
    assert get_status_code(response) == HTTPStatus.CREATED, 'Expected HTTP status is 201'
    appLogger.debug('Assert response content equal to send data')
    assert response.json() == data_to_post, 'Response and posted data are not equal'

    appLogger.debug('Make GET request for users/')
    response = get_users(str(test_data['user_5']['id']))
    appLogger.debug('Assert response status code is 200')
    assert get_status_code(response) == HTTPStatus.OK, 'Expected HTTP status is 200'
    appLogger.debug('Assert response is Json')
    user_data = response.json()
    assert user_data, 'response is not in JSON'
    appLogger.debug('Assert collected data for user 5')
    assert user_data == test_data['user_5'], 'Users data are not equal'

