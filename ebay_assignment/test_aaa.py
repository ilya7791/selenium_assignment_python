from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def test_add_items_till_reach_price_500():

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)