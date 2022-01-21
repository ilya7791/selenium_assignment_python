from selenium.webdriver.common.by import By

from ebay_assignment.pages.base_page import BasePage


class SamsungGalleryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.galaxy_note_10 = (By.CSS_SELECTOR,
                               "#mainContent > section:nth-child(1) > div.b-visualnav__grid > a:nth-child(1)")  # #Samsung Galaxy Note 10
        self.t_mobile_filter = (By.CSS_SELECTOR, "div.carousel li:nth-child(3) > a")

    def select_galaxy_note_10(self):
        self.click(self.galaxy_note_10)

    def select_t_mobile_filter(self):
        self.click(self.t_mobile_filter)
