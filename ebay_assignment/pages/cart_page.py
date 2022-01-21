from selenium.webdriver.common.by import By

from ebay_assignment.pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.subtotal_price = (By.CSS_SELECTOR, "[data-test-id ='SUBTOTAL']")
        self.checkout_btn = (By.CSS_SELECTOR, "[data-test-id ='cta-top']")
        self.continue_as_guest_btn = (By.CSS_SELECTOR, "[class ='dialog__body']>:nth-child(2)")

    def get_subtotal_price(self):
        subtotal_str = self.get_text(self.subtotal_price).replace("US $", "").replace(".00", "")
        subtotal_price = float(subtotal_str)
        return subtotal_price

    def click_checkout_btn(self):
        self.click(self.checkout_btn)

    def click_continue_as_guest_btn(self):
        self.click(self.continue_as_guest_btn)
