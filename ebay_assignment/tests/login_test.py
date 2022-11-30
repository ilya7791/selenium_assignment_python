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

from ebay_assignment.pages.login_page import LoginPage
from ebay_assignment.tests.base_test import BaseTest


class TestLogin(BaseTest):

    # checks that a correct error message appears after incorrect login attempt
    def test_empty_username_and_password(self):
        login = LoginPage(self.driver)
        self.driver.find_element("css selector","[data-track='gnSignin']").click()
        self.driver.find_element("id", "login-email").send_keys("ilya7791@gmail.com")
        self.driver.find_element("css selector", "[class='user-select-none']").click()
        self.driver.find_element("id", "login-password").send_keys("vjm9wUiu123@")
        self.driver.find_element("css selector", "[class='user-select-none']").click()

        self.driver.find_element("id", "search-field").send_keys("cat")
        self.driver.find_element("id", "search-field").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element("css selector", "[data-track='search-toggle-advanced']").click()
        time.sleep(3)
        # self.driver.find_element("css selector", "[data-orientation-value='landscape']").click()
        self.driver.find_element("css selector", "[data-orientation-value='portrait']").click()
        time.sleep(3)
        self.driver.find_element("css selector", "[data-orientation-value='square']").click()
        time.sleep(3)
        self.driver.find_element("css selector", "[data-orientation-value='panorama']").click()
        time.sleep(3)

        items = self.driver.find_elements("css selector", "[class='view photo-list-view']>*")
        for item in items:
            stile=item.get_attribute("style")

            stile_parts = stile.split()
            width = int(stile_parts[4].replace("px;", ""))
            height = int(stile_parts[6].replace("px;", ""))
            width = int(stile_parts[6].replace("px;", ""))
            # width = int(x.split(";")[1].replace("width: ", "").replace("px", ""))
            # height = int(x.split(";")[2].replace("heigt: ", "").replace("px", ""))
            # item.get_attribute("style")
        # time.sleep(5)
        # orientation_list=self.driver.find_elements("css selector", "[class='orientation-list']>*")
        # for button in orientation_list:
        #     # button.find_element("css selector", "div").click()
        #     button.click()

        # self.driver.find_element("css selector", "user-select-none").click()

        # self.driver.find_element("id selector", "login-email").send_keys("login-email")

        # self.driver.find_element_by_css_selector("li.gn-signin.tablet-and-desktop-only > a").click()
        # self.driver.find_element("css selector","li.gn-signin.tablet-and-desktop-only > a").click()
        # "driver.find_element("css selector", SELECTOR)"
        time.sleep(100)
        login.enter_password()

        # login.enter_user_credentials(TestParams.EMPTY_USERNAME, TestParams.EMPTY_PASSWORD)
        # error_msg = login.get_error_login_msg()
        #
        # # verifying that error message  is correct
        # Logger.log(f"error_msg: {error_msg}", headline=True)
        # # self.driver.find_element_by_css_selector("[data-id=login-username] input").send_keys("aaaaa")
        # assert TestParams.INCORRECT_LOGIN_CREDENTIALS_MSG in error_msg

    # def test_empty_username_correct_password(self):
    #     login = LoginPage(self.driver)
    #     Logger.log(f"The parameters for login are: {TestParams.EMPTY_USERNAME} , {TestParams.CORRECT_PASSWORD}",
    #                headline=True)
    #     login.enter_user_credentials(TestParams.EMPTY_USERNAME, TestParams.CORRECT_PASSWORD)
    #     error_msg = login.get_error_login_msg()
    #     Logger.log(f"error_msg: {error_msg}", headline=True)
    #     assert TestParams.INCORRECT_LOGIN_CREDENTIALS_MSG in error_msg
    #
    # def test_correct_username_empty_password(self):
    #     login = LoginPage(self.driver)
    #     Logger.log(f"The parameters for login are: {TestParams.CORRECT_USERNAME} , {TestParams.EMPTY_PASSWORD}",
    #                headline=True)
    #     login.enter_user_credentials(TestParams.CORRECT_USERNAME, TestParams.EMPTY_PASSWORD)
    #     error_msg = login.get_error_login_msg()
    #     Logger.log(f"error_msg: {error_msg}", headline=True)
    #     assert TestParams.INCORRECT_LOGIN_CREDENTIALS_MSG in error_msg
    #
    # def test_incorrect_username_and_password(self):
    #     login = LoginPage(self.driver)
    #     Logger.log(f"The parameters for login are: {TestParams.INCORRECT_USERNAME} , {TestParams.INCORRECT_PASSWORD}",
    #                headline=True)
    #     login.enter_user_credentials(TestParams.INCORRECT_USERNAME, TestParams.INCORRECT_PASSWORD)
    #     error_msg = login.get_error_login_msg()
    #     Logger.log(f"error_msg: {error_msg}", headline=True)
    #     assert TestParams.INCORRECT_LOGIN_CREDENTIALS_MSG in error_msg
    #
    # def test_incorrect_username_correct_password(self):
    #     login = LoginPage(self.driver)
    #     Logger.log(f"The parameters for login are: {TestParams.INCORRECT_USERNAME} , {TestParams.CORRECT_PASSWORD}",
    #                headline=True)
    #     login.enter_user_credentials(TestParams.INCORRECT_USERNAME, TestParams.CORRECT_PASSWORD)
    #     error_msg = login.get_error_login_msg()
    #     Logger.log(f"error_msg: {error_msg}", headline=True)
    #     assert TestParams.INCORRECT_LOGIN_CREDENTIALS_MSG in error_msg
    #
    # def test_correct_username_incorrect_password(self):
    #     login = LoginPage(self.driver)
    #     Logger.log(f"The parameters for login are: {TestParams.CORRECT_USERNAME} , {TestParams.INCORRECT_PASSWORD}",
    #                headline=True)
    #     login.enter_user_credentials(TestParams.CORRECT_USERNAME, TestParams.INCORRECT_PASSWORD)
    #     error_msg = login.get_error_login_msg()
    #     Logger.log(f"error_msg: {error_msg}", headline=True)
    #     assert TestParams.INCORRECT_LOGIN_CREDENTIALS_MSG in error_msg
    #
    # def test_correct_username_uppercase_password(self):
    #     login = LoginPage(self.driver)
    #     Logger.log(f"The parameters for login are: {TestParams.CORRECT_USERNAME} , {TestParams.UPPERCASE_PASSWORD}",
    #                headline=True)
    #     login.enter_user_credentials(TestParams.CORRECT_USERNAME, TestParams.UPPERCASE_PASSWORD)
    #     error_msg = login.get_error_login_msg()
    #     Logger.log(f"error_msg: {error_msg}", headline=True)
    #     assert TestParams.INCORRECT_LOGIN_CREDENTIALS_MSG in error_msg
    #
    # def test_check_user_place_holder(self):
    #     login = LoginPage(self.driver)
    #     place_holder_txt = login.get_username_textbox()
    #     Logger.log(f"place_holder_txt: {place_holder_txt}", headline=True)
    #     assert place_holder_txt == TestParams.LOGIN_PLACE_HOLDER
    #
    # def test_username_and_password_with_spaces(self):
    #     login = LoginPage(self.driver)
    #     Logger.log(
    #         f"The parameters for login are: {TestParams.WITH_SPACES_USERNAME} , {TestParams.WITH_SPACES_PASSWORD}",
    #         headline=True)
    #     login.enter_user_credentials(TestParams.WITH_SPACES_USERNAME, TestParams.WITH_SPACES_PASSWORD)
    #     error_msg = login.get_error_login_msg()
    #     Logger.log(f"error_msg: {error_msg}", headline=True)
    #     assert TestParams.INCORRECT_LOGIN_CREDENTIALS_MSG in error_msg
    #
    # def test_login_with_string_terminator_username(self):
    #     login = LoginPage(self.driver)
    #     Logger.log(
    #         f"The parameters for login are: {TestParams.WITH_STRING_TERMINATOR_USERNAME} , {TestParams.CORRECT_PASSWORD}",
    #         headline=True)
    #     login.enter_user_credentials(TestParams.WITH_STRING_TERMINATOR_USERNAME, TestParams.CORRECT_PASSWORD)
    #     error_msg = login.get_error_login_msg()
    #     Logger.log(f"error_msg: {error_msg}", headline=True)
    #     assert TestParams.INCORRECT_LOGIN_CREDENTIALS_MSG in error_msg
    #
    # def test_login_with_string_terminator_password(self):
    #     login = LoginPage(self.driver)
    #     Logger.log(
    #         f"The parameters for login are: {TestParams.CORRECT_USERNAME} , {TestParams.WITH_STRING_TERMINATOR_PASSWORD}",
    #         headline=True)
    #     login.enter_user_credentials(TestParams.CORRECT_USERNAME, TestParams.WITH_STRING_TERMINATOR_PASSWORD)
    #     error_msg = login.get_error_login_msg()
    #     Logger.log(f"error_msg: {error_msg}", headline=True)
    #     assert TestParams.INCORRECT_LOGIN_CREDENTIALS_MSG in error_msg
    #
    # def test_click_login_after_logout(self):
    #     login = LoginPage(self.driver)
    #     Logger.log(f"The parameters for login are: {TestParams.CORRECT_USERNAME} , {TestParams.CORRECT_PASSWORD}",
    #                headline=True)
    #     login.enter_user_credentials(TestParams.CORRECT_USERNAME, TestParams.CORRECT_PASSWORD)
    #     navigation_bar = NavigationBarPage(self.driver)
    #     Logger.log(f"logging out", headline=True)
    #     navigation_bar.logout()
    #
    #     # verifying that unable to login after clicking "login" after logout
    #     Logger.log(f"logging in", headline=True)
    #     login.click_login_button()
    #     error_msg = login.get_error_login_msg()
    #     Logger.log(f"error_msg: {error_msg}", headline=True)
    #     assert TestParams.INCORRECT_LOGIN_CREDENTIALS_MSG in error_msg
    #
    # def test_login_with_long_user_name_and_password(self):
    #     login = LoginPage(self.driver)
    #     Logger.log(f"The parameters for login are: {TestParams.LONG_USERNAME} , {TestParams.LONG_PASSWORD}",
    #                headline=True)
    #     login.enter_user_credentials(TestParams.LONG_USERNAME, TestParams.LONG_PASSWORD)
    #     error_msg = login.get_error_login_msg()
    #     Logger.log(f"error_msg: {error_msg}", headline=True)
    #     assert TestParams.INCORRECT_LOGIN_CREDENTIALS_MSG in error_msg