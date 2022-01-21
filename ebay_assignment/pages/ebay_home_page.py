from selenium.webdriver.common.by import By

from ebay_assignment.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.sumsung_devices = (By.CSS_SELECTOR, "#destinations_list1 > ul > li:nth-child(2) > a > div > div > div")

    def select_samsung_category(self):
        self.click(self.sumsung_devices)
