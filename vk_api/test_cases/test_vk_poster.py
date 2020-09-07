from framework.pageobject.pages import VkAuthPage, VkUserPage
from framework.logger import appLogger
from framework.utils.APIutils import *
from framework.utils.assistance import *

config_data = get_config_data()
test_data = get_test_data()
LOGIN = test_data['vk_login']
PASSWORD = test_data['vk_pass']
TOKEN = test_data['vk_token']
IMAGE = test_data['img_path']


def test_vk_poster(browser):
    appLogger.debug('Opening browser')
    vk_auth_page = VkAuthPage(browser)
    appLogger.debug('Open', config_data['url'])
    vk_auth_page.go_to_site(config_data['url'])

    appLogger.debug('Enter user login')
    vk_auth_page.enter_login(LOGIN)
    appLogger.debug('Enter user password')
    vk_auth_page.enter_password(PASSWORD)
    appLogger.debug('Click "Log in" button')
    vk_auth_page.click_enter_button()

    user_page = VkUserPage(browser)
    appLogger.debug('Go to personal page')
    user_page.click_personal_page()
    appLogger.debug('Creating wall post')
    message = generate_string()
    wallpost = create_wallpost(message)['response']['post_id']
    personal_wallpost = f"{USER_ID}_{wallpost}"
    appLogger.debug('Searching for post')
    assert user_page.find_user_post(message), 'Post is not created'

    appLogger.debug('Upload photo')
    photo = upload_wallpost_photo(IMAGE)
    appLogger.debug('Edit last post on wall')
    new_message = generate_string()
    appLogger.debug('Edit wallpost')
    edit_wallpost(wallpost, new_message, photo)

    pic_attr = user_page.get_picture_attribute(f'{USER_ID}_{photo}')
    pic_url = match_url(pic_attr)
    download_file(pic_url)

    appLogger.debug('Search for edited post with picture')
    assert user_page.find_user_post(new_message), "Incorrect message in updated post"
    assert compare_images('../compare.jpg', IMAGE) is None, 'Images is not equal'

    appLogger.debug('Add comment to post')
    comment = generate_string()
    add_post_comment(wallpost, comment)

    appLogger.debug('Click show post replies')
    user_page.show_post_comments(personal_wallpost)

    appLogger.debug('Assert new comment by user')
    assert user_page.find_user_post(comment), 'Comment is not found'
    appLogger.debug('Assert comment added by user')
    assert user_page.get_commentator_id(personal_wallpost, USER_ID)

    appLogger.debug('Click like button')
    user_page.click_like_btn(personal_wallpost)
    appLogger.debug('Check like under post')
    assert USER_ID in check_post_like(wallpost), "Like button was not clicked"

    appLogger.debug('Delete post')
    delete_wallpost(wallpost)
    appLogger.debug('Assert that post deleted')
    assert user_page.find_deleted_post(personal_wallpost), "Post was not deleted"
