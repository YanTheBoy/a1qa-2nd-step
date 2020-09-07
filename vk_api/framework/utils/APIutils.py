from framework.utils.assistance import get_config_data, get_test_data, generate_string
import requests
test_data = get_test_data()
config_data = get_config_data()


API_VERSION = 5.122
URL = config_data['url']
USER_ID = test_data['user_id']
API_METHOD = 'https://api.vk.com/method/'
TOKEN = test_data['vk_token']
WALL_POST = 'wall.post'
EDIT_POST = 'wall.edit'
GET_PIC_SERVER = 'photos.getWallUploadServer'
SAVE_WALL_PIC = 'photos.saveWallPhoto'
ADD_COMMENT = 'wall.createComment'
LIKES = 'likes.getList'
DELETE = 'wall.delete'
params = {'access_token': TOKEN,
          'v': API_VERSION}


def delete_wallpost(post_id):
    response = requests.get(
        f'{API_METHOD}{DELETE}?'
        f'owner_id={USER_ID}&post_id={post_id}',
        params=params).json()
    return response


def create_wallpost(message):
    response = requests.post(
        f'{API_METHOD}{WALL_POST}?'
        f'owner_id={USER_ID}&message={message}',
        params=params).json()
    return response


def upload_wallpost_photo(image):
    upl_server_response = requests.get(
        f'{API_METHOD}{GET_PIC_SERVER}', params=params).json()

    upload_pic_response = requests.post(
        upl_server_response['response']['upload_url'],
        params={'access_token': TOKEN},
        files={'photo': open(image, 'rb')}).json()

    save_pic_response = requests.get(
        f'{API_METHOD}{SAVE_WALL_PIC}?user_id={USER_ID}&'
        f'photo={upload_pic_response["photo"]}&'
        f'hash={upload_pic_response["hash"]}&'
        f'server={upload_pic_response["server"]}',
        params=params).json()
    return save_pic_response["response"][0]["id"]


def add_post_comment(post_id, comment):
    request = requests.get(
        f'{API_METHOD}{ADD_COMMENT}?owner_id={USER_ID}&'
        f'post_id={post_id}&'
        f'message={comment}',
        params=params).json()
    return request


def edit_wallpost(post_id, message, attachment=None):
    attachment = f'photo{USER_ID}_{attachment}'
    request = requests.post(
        f'{API_METHOD}{EDIT_POST}?'
        f'owner_id={USER_ID}&message={message}&'
        f'attachment={attachment}&post_id={post_id}',
        params=params).json()
    return request


def download_file(url):
    response = requests.get(url)
    file = open("../compare.jpg", "wb")
    file.write(response.content)
    file.close()


def check_post_like(post_id):
    response = requests.get(
        f'{API_METHOD}{LIKES}?'
        f'type=post&owner_id={USER_ID}&'
        f'item_id={post_id}',
        params=params).json()
    return response['response']['items']


