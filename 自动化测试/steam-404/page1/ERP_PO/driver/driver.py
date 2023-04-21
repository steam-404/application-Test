from selenium import webdriver


class Driver:
    @staticmethod
    def get_url():
        return webdriver.Chrome()
