class BaseEntity:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def complete_basic_auth(self, url, login, password):
        self.go_to_site(
            url.replace(
                'https://', f'https://{login}:{password}@'))
