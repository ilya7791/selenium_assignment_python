# from classes.login_tests.pages.login_page import LoginPage
# from classes.login_tests.pages.navigation_bar_page import NavigationBarPage
# from classes.login_tests.params.parameters import TestParams
# from classes.login_tests.tests.base_test import BaseTest
# from utils.error_handling import Logger

# Logger("log_test.log", debug=True)


# username_input = (By.CSS_SELECTOR, "[data-id=login-username] input")
# password_input = (By.CSS_SELECTOR, "[data-id=login-password] input")

# TODO Ilya: PEP 8 here and in all other modules
import time

from selenium.webdriver import Keys

from ebay_assignment.pages.home_page import HomePage
from ebay_assignment.pages.login_page import LoginPage
from ebay_assignment.tests.base_test import BaseTest


class TestLogin(BaseTest):

    # checks that a correct error message appears after incorrect login attempt
    def test_empty_username_and_password(self):
        login = LoginPage(self.driver)
        home = HomePage(self.driver)
        login.perform_login("ilya7791@gmail.com", "vjm9wUiu123@")
        home.search_tag("cat")
        # time.sleep(3)
        home.click_advanced_btn()
        home.set_landscape_filter()
        items=home.get_items()

        count = 1
        for item in items:
            if count == 20:
                break
            width = home.get_item_style_num(item, style_part=4)
            height = home.get_item_style_num(item, style_part=6)
            print("aaaaaadfdaaaaaaa")
            print("height:" + str(height))
            count += 1
            assert width > height
            # assert width < height
            # assert width == height
            # assert width > 2 * height


