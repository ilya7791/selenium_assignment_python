import time

from ebay_assignment.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # self.username_input = Locators.username_input
        self.password_input = "forgot-password-confirm-password"
        # self.driver.find_element_by_css_selector("[data-track='gnSignin']").click()
        # self.driver.find_element_by_css_selector("li.gn-signin.tablet-and-desktop-only > a").click()


        # self.login_btn = Locators.login_btn
        # self.login_error_msg = Locators.login_error_msg
        # self.view_demo_link = Locators.view_demo_link

    # def enter_username(self, user_name):
    #     self.send_text(self.username_input, user_name)


    def click_login(self):
        self.click("yui_3_16_0_1_1669756177362_492")


    def enter_password(self):
        # self.send_text(self.password_input, user_password)
        self.send_text(self.password_input, "vjm9wUiu123@")
        time.sleep(999)

    # def enter_password_and_enter(self, user_password):
    #     self.send_text_and_enter(self.password_input, user_password)
    #
    # def click_login_button(self):
    #     self.click(self.login_btn)
    #
    # def enter_user_credentials(self, user_name, password):
    #     self.enter_username(user_name)
    #     self.enter_password(password)
    #     self.click_login_button()
    #     time.sleep(1)
    #
    # def get_error_login_msg(self):
    #     time.sleep(1)
    #     error_msg = self.get_text(self.login_error_msg)
    #     return error_msg
    #
    # def get_username_textbox(self):
    #     # example getting text: text = self.driver.find_element_by_css_selector("[data-id=login-username] input").get_attribute('placeholder')
    #     text = self.get_element(self.username_input).get_attribute('placeholder')
    #     return text
    #
    # def open_view_demo_page(self):
    #     self.click(self.view_demo_link)
    #     self.switch_to_new_windows()