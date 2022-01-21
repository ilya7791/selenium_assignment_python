from selenium.webdriver.common.by import By

from ebay_assignment.pages.base_page import BasePage


class SamsungNot10GalleryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.items = (By.CSS_SELECTOR, "#mainContent section>:nth-child(3) li")
        self.price_filter_btn = (By.CSS_SELECTOR, "[class ='brm__list'] >:nth-child(8) button")
        self.price_under = (By.CSS_SELECTOR, "[class ='brm__list'] >:nth-child(8)>div>:nth-child(2)>ul a")


    def select_galaxy_note_10_items(self):
        return self.get_elements(self.items)

    def select_item(self, item_in_gallery):
        item_in_gallery.find_element_by_tag_name("div").click()


    def click_price_filter(self):
        self.click(self.price_filter_btn)

    def select_price_filter_under(self):
        self.click_price_filter()
        self.click(self.price_under)

