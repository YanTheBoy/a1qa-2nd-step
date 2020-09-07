from framework.base.default_page import BasePage
from selenium.webdriver.common.by import By
from .element import Button, BaseElement
from string import Template



class VkAuthPageLocators:
    LOGIN = (By.ID, 'index_email')
    PASSWORD = (By.ID, 'index_pass')
    LOG_IN_BTN = (By.ID, 'index_login_button')


class VkAuthPage(BasePage):
    def enter_login(self, login):
        login_field = BaseElement(VkAuthPageLocators.LOGIN, self.driver)
        login_field.send_keys(login)

    def enter_password(self, password):
        pass_field = BaseElement(VkAuthPageLocators.PASSWORD, self.driver)
        pass_field.send_keys(password)

    def click_enter_button(self):
        Button(VkAuthPageLocators.LOG_IN_BTN, self.driver).click()


class VkUserPageLocators:
    PERSONAL_PAGE = (By.ID, 'l_pr')
    POST = (Template('//*[contains(text(), "$message")]'))
    POST_PICTURE = (Template('//*[@data-photo-id="$pic_id"]'))
    COMMENTATOR = (Template('//*[@id="post$post"]//a[@data-from-id="$owner_id"]'))
    LIKE_BTN = (Template('//*[@id="post$post"]//div[@class="like_button_icon"]'))
    POST_REPLIES = (Template('//*[@id="replies$post"]/a'))
    DEL_POST = (Template('//*[@id="post$post"]/div[@style="display: none;"]'))


class VkUserPage(BasePage):
    def find_deleted_post(self, post):
        locator = (By.XPATH, VkUserPageLocators.DEL_POST.substitute(post=post))
        return self.find_invisible_element(locator)

    def click_like_btn(self, post_id):
        locator = (By.XPATH, VkUserPageLocators.LIKE_BTN.substitute(post=post_id))
        Button(locator, self.driver).click()

    def click_personal_page(self):
        Button(VkUserPageLocators.PERSONAL_PAGE, self.driver).click()

    def find_user_post(self, message):
        locator = (By.XPATH, VkUserPageLocators.POST.substitute(message=message))
        return self.find_element(locator)

    def get_picture_attribute(self, pic_id):
        locator = (By.XPATH, VkUserPageLocators.POST_PICTURE.substitute(pic_id=pic_id))
        return BaseElement(locator, self.driver).get_attribute('onclick')

    def get_commentator_id(self, post_id, user_id):
        locator = (By.XPATH, VkUserPageLocators.COMMENTATOR.substitute(
            post=post_id, owner_id=user_id))
        return self.find_element(locator)

    def show_post_comments(self, replies):
        locator = (By.XPATH, VkUserPageLocators.POST_REPLIES.substitute(post=replies))
        return Button(locator, self.driver).click()
