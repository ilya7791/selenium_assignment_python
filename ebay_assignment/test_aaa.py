from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def test_add_items_till_reach_price_500():
    count = 20
    print(f"count: {count}")
