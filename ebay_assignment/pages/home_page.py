import time

from selenium.webdriver.common.by import By

from ebay_assignment.pages.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_box = (By.ID, "search-field")
        self.advanced_btn = (By.CSS_SELECTOR, "[data-track='search-toggle-advanced']")
        self.landscape_filter = (By.CSS_SELECTOR, "[data-orientation-value='landscape']")
        self.portrait_filter = (By.CSS_SELECTOR, "[data-orientation-value='portrait']")
        self.square_filter = (By.CSS_SELECTOR, "[data-orientation-value='square']")
        self.panorama_filter = (By.CSS_SELECTOR, "[data-orientation-value='panorama']")
        self.items = (By.CSS_SELECTOR, "[class='view photo-list-view']>*")


    def get_items(self):
        return self.get_elements(self.items)

    def search_tag(self, tag_name):
        self.send_text_and_enter(self.search_box, tag_name)
        time.sleep(3)

    def click_advanced_btn(self):
        self.click(self.advanced_btn)
        time.sleep(1)

    def click_landscape_filter(self):
        self.click(self.landscape_filter)
        time.sleep(3)

    def click_portrait_filter(self):
        self.click(self.portrait_filter)
        time.sleep(3)

    def click_square_filter(self):
        self.click(self.square_filter)
        time.sleep(3)

    def click_panorama_filter(self):
        self.click(self.panorama_filter)
        time.sleep(3)

    def set_landscape_filter(self):
        self.click_portrait_filter()
        self.click_square_filter()
        self.click_panorama_filter()

    def set_portrait_filter(self):
        self.click_landscape_filter()
        self.click_square_filter()
        self.click_panorama_filter()

    def set_square_filter(self):
        self.click_portrait_filter()
        self.click_landscape_filter()
        self.click_panorama_filter()

    def set_panorama_filter(self):
        self.click_portrait_filter()
        self.click_landscape_filter()
        self.click_square_filter()

    def get_item_style_num(self, item, style_part):
        stile = item.get_attribute("style")
        style_parts = stile.split()
        style_num = int(style_parts[style_part].replace("px;", ""))
        return style_num


#item=width