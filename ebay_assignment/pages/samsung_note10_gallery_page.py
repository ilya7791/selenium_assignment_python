from selenium.webdriver.common.by import By

from ebay_assignment.pages.base_page import BasePage


class SamsungNot10GalleryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.items = (By.CSS_SELECTOR, "div.carousel>div>:nth-child(2)>ul li")

    def select_galaxy_note_10_items(self):
        return self.get_elements(self.items)

    def select_item(self, item_in_gallery):
        item_in_gallery.find_element_by_tag_name("a").click()
