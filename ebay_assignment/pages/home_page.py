import random
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
        self.title_view = (By.CSS_SELECTOR, "[data-layout-style='til']")
        self.random_item = (By.CSS_SELECTOR, f"[class='view photo-list-view']>:nth-child({random.randint(20, 20)}")
        self.item_title_in_gallery = (By.CSS_SELECTOR, "[class='metadata']>:nth-child(1)")
        self.item_user_in_gallery = (By.CSS_SELECTOR, "[class='metadata']>:nth-child(2)")
        self.item_stars_count_in_item_page = (By.CSS_SELECTOR, "[class='fave-count-label']")
        self.item_comments_count_in_item_page = (By.CSS_SELECTOR, "[class='comment-count-label']")
        self.item_user_and_galleryin_item_page = (By.CSS_SELECTOR, "[class='sub-photo-content-container']")

    def get_item_user_and_gallery_in_item_page(self):
        return self.get_text(self.item_user_and_galleryin_item_page)
    def get_item_comments_count_in_item_page(self):
        return self.get_text(self.item_comments_count_in_item_page)
    def get_item_stars_count_in_item_page(self):
        return self.get_text(self.item_stars_count_in_item_page)
    def get_item_user_in_gallery(self):
        return self.get_text(self.item_user_in_gallery).replace("by ","")
    def get_item_title_in_gallery(self):
        return self.get_text(self.item_title_in_gallery)
    def get_random_item(self):
        return self.get_element(self.random_item)

    def get_items(self):
        return self.get_elements(self.items)

    def click_title_view(self):
        self.click(self.title_view)
        time.sleep(3)
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


    def open_advance_filer_for_tag(self, tag_name):
        self.search_tag(tag_name)
        self.click_advanced_btn()
