from selenium.webdriver.common.by import By
from ebay_assignment.pages.home_page import HomePage
from ebay_assignment.pages.login_page import LoginPage
from ebay_assignment.params.parameters import TestParams
from ebay_assignment.tests.base_test import BaseTest

class TestLogin(BaseTest):

    def test_ilya(self):
        login = LoginPage(self.driver)
        home = HomePage(self.driver)
        login.perform_login(TestParams.USERNAME, TestParams.PASSWORD)
        home.search_tag(TestParams.TAG_TO_SEARCH)
        home.click_title_view()
        image = home.get_random_item()
        item_title_in_gallery = image.find_element(By.CSS_SELECTOR, "[class='metadata']>:nth-child(1)").text
        item_user_in_gallery = image.find_element(By.CSS_SELECTOR, " [class='metadata']>:nth-child(2)").text.replace("by ","")
        item_stars_count_in_gallery = image.find_element(By.CSS_SELECTOR, "[class='engagement']>:nth-child(1)").text
        item_comments_count_in_gallery = image.find_element(By.CSS_SELECTOR, "[class='engagement']>:nth-child(2)").text
        image.find_element(By.CSS_SELECTOR, "a").click()
        item_stars_count_in_item_page=home.get_item_stars_count_in_item_page()
        item_comments_count_in_item_page=home.get_item_comments_count_in_item_page()
        item_user_and_galleryin_item_page = home.get_item_user_and_gallery_in_item_page()

        assert item_stars_count_in_gallery == item_stars_count_in_item_page
        assert item_comments_count_in_gallery == item_comments_count_in_item_page
        assert item_title_in_gallery in item_user_and_galleryin_item_page
        assert item_user_in_gallery in item_user_and_galleryin_item_page

