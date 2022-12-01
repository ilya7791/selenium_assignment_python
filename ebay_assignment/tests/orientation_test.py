import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from ebay_assignment.pages.home_page import HomePage
from ebay_assignment.pages.login_page import LoginPage
from ebay_assignment.params.parameters import TestParams
from ebay_assignment.tests.base_test import BaseTest


class TestLogin(BaseTest):
    def test_orientation_filter(self):
        login = LoginPage(self.driver)
        home = HomePage(self.driver)
        login.perform_login(TestParams.USERNAME, TestParams.PASSWORD)
        home.open_advance_filer_for_tag(TestParams.TAG_TO_SEARCH)
        #
        # # self.driver.execute_script("document.querySelector('" + cssSelector + "').click()")
        # # cssSelector="[class='photo-list-photo-interaction']"
        # # self.driver.execute_script("document.querySelector('" + cssSelector + "').click()")
        #
        # # a = ActionChains(self.driver)
        # # element=self.driver.find_element(By.CSS_SELECTOR, "[class='photo-list-photo-interaction']")
        # # a.move_to_element(element).perform()
        # #
        # # element = self.driver.find_element(By.CSS_SELECTOR, "[class='overlay no-outline']")
        # # self.driver.execute_script("arguments[0].click()", element)
        # #
        # # # self.driver.execute_script("document.querySelector('[class='photo-list-photo-interaction']').text")
        # #
        # #
        # # m = self.driver.find_element(By.CSS_SELECTOR, "[class='photo-list-photo-interaction']")
        # # mm=m.text
        # # m = self.driver.find_element(By.CSS_SELECTOR, "[class='title no-outline']")
        # # a.move_to_element(m).perform()
        # self.driver.find_element(By.CSS_SELECTOR, "[data-layout-style='til']").click()
        # home.click_title_view()
        #
        #
        # # s = self.driver.find_element(By.CSS_SELECTOR, "[class='interaction-bar']")
        # # s = self.driver.find_element(By.CSS_SELECTOR, "[class='interaction-bar']").text
        #
        # #
        # # s=self.driver.find_element(By.CSS_SELECTOR, "[class='title no-outline']").text
        # # d = self.driver.find_element(By.CSS_SELECTOR, "[class='metadata']")
        # # title=d.find_element(By.CSS_SELECTOR, "div").text
        # # by=   d.find_element(By.CSS_SELECTOR, ":nth-child(2)").text
        #
        # image=self.driver.find_element(By.CSS_SELECTOR, "[class='view photo-list-view']>:nth-child(1)")
        # item_title_in_gallery=image.find_element(By.CSS_SELECTOR, "[class='metadata']>:nth-child(1)").text
        # item_user_in_gallery = image.find_element(By.CSS_SELECTOR, " [class='metadata']>:nth-child(2)").text.replace("by ","")
        #
        #
        # item_stars_count_in_gallery = image.find_element(By.CSS_SELECTOR, "[class='engagement']>:nth-child(1)").text
        # item_comments_count_in_gallery = self.driver.find_element(By.CSS_SELECTOR, "[class='engagement']>:nth-child(2)").text
        #
        # image.find_element(By.CSS_SELECTOR, "a").click()
        # time.sleep(2)
        # item_stars_count_in_item_page = self.driver.find_element(By.CSS_SELECTOR, "[class='fave-count-label']").text
        # item_comments_count_in_item_page = self.driver.find_element(By.CSS_SELECTOR, "[class='comment-count-label']").text
        #
        # item_user_and_galleryin_item_page = self.driver.find_element(By.CSS_SELECTOR,
        #                                                   "[class='sub-photo-content-container']").text
        #
        # assert item_stars_count_in_gallery == item_stars_count_in_item_page
        # assert item_comments_count_in_gallery == item_comments_count_in_item_page
        # #assert item_title_in_gallery  in item_user_and_galleryin_item_page and item_user_in_gallery in item_user_and_galleryin_item_page
        # assert item_title_in_gallery in item_user_and_galleryin_item_page
        # assert item_user_in_gallery in item_user_and_galleryin_item_page
        #
        # # item_user_in_item_page = self.driver.find_element(By.CSS_SELECTOR, "[class='owner-name truncate no-outline']").text
        # # item_title_in_item_page = self.driver.find_element(By.CSS_SELECTOR, "[class=' meta-field photo-title ']").text
        # #
        #
        # # test landscape orientation filter
        home.set_landscape_filter()
        items = home.get_items()
        count = 1
        for item in items:
            if count < 20:
                print(f"count: {count}")
                width = home.get_item_style_num(item, style_part=4)
                height = home.get_item_style_num(item, style_part=6)
                assert width > height
                count += 1
            else:
                break

        # test portrait orientation filter
        home.click_portrait_filter()
        home.click_landscape_filter()
        items = home.get_items()
        count = 1
        for item in items:
            if count < 20:
                print(f"count: {count}")
                width = home.get_item_style_num(item, style_part=4)
                height = home.get_item_style_num(item, style_part=6)
                count += 1
                assert width < height
                count += 1
            else:
                break

        # test square orientation filter
        home.click_square_filter()
        home.click_portrait_filter()
        items = home.get_items()
        count = 1
        for item in items:
            if count < 20:
                print(f"count: {count}")
                width = home.get_item_style_num(item, style_part=4)
                height = home.get_item_style_num(item, style_part=6)
                count += 1
                assert width == height, "width is not equal to height"
                count += 1
            else:
                break

        # test panorama orientation filter
        home.click_panorama_filter()
        home.click_square_filter()
        items = home.get_items()
        count = 1
        for item in items:
            if count < 20:
                print(f"count: {count}")
                width = home.get_item_style_num(item, style_part=4)
                height = home.get_item_style_num(item, style_part=6)
                assert width > height * 2
                count += 1
            else:
                break
