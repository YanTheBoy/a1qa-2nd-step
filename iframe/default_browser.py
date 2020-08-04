class BaseEntity:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

