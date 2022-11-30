import time

from ebay_assignment.pages.cart_page import CartPage
from ebay_assignment.pages.ebay_home_page import HomePage
from ebay_assignment.pages.item_page import ItemPage
from ebay_assignment.pages.samsung_gallery_page import SamsungGalleryPage
from ebay_assignment.pages.samsung_note10_gallery_page import SamsungNot10GalleryPage
from ebay_assignment.params.parameters import TestParams
from ebay_assignment.tests.base_test import BaseTest

class TestEbay(BaseTest):

    def test_add_items_till_reach_price_500(self):
        home_page_obj = HomePage(self.driver)
        time.sleep(999)
        # home_page_obj.select_samsung_category()
        #
        # gallery_obj = SamsungGalleryPage(self.driver)
        # gallery_obj.select_galaxy_note_10()
        # gallery_obj.select_t_mobile_filter()
        #
        # items_not_10_obj = SamsungNot10GalleryPage(self.driver)
        # items_not_10_obj.select_price_filter_under()
        # subtotal_price = 0
        # seen_items_num = []
        # while subtotal_price < TestParams.MAX_TOTAL_PRICE:
        #     item_num = 0
        #     items_not_10_obj = SamsungNot10GalleryPage(self.driver)
        #     items_not_10 = items_not_10_obj.select_galaxy_note_10_items()
        #     for item in items_not_10:
        #
        #         if item_num not in seen_items_num:
        #             item.find_element_by_tag_name("div").click()  # select item in gallery
        #             item_page_obj = ItemPage(self.driver)
        #             item_page_obj.add_to_cart()
        #             cart_page_obj = CartPage(self.driver)
        #             subtotal_price = cart_page_obj.get_subtotal_price()
        #             if subtotal_price > TestParams.MAX_TOTAL_PRICE:
        #                 break
        #             else:
        #                 seen_items_num.append(item_num)
        #                 self.driver.back()
        #                 self.driver.back()
        #             break
        #         else:
        #             item_num = +1
        #
        # cart_page_obj = CartPage(self.driver)
        # cart_page_obj.click_checkout_btn()
        # cart_page_obj.click_continue_as_guest_btn()
