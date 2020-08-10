class BaseEntity:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def get_cookies(self):
        return self.driver.get_cookies()

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def delete_cookie(self, name):
        return self.driver.delete_cookie(name)

    def delete_cookies(self):
        return self.driver.delete_all_cookies()

    def add_cookies(self, cookies):
        for name, value in cookies.items():
            self.driver.add_cookie({
                'name': name,
                'value': value
            })
