from selenium.webdriver.common.by import By

from ebay_assignment.pages.base_page import BasePage


class ItemPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_btn = (By.ID, "isCartBtn_btn")

    def add_to_cart(self):
        self.click(self.add_to_cart_btn)
