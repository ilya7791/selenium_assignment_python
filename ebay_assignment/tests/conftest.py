import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from ebay_assignment.params.parameters import TestParams


@pytest.fixture(scope="session")
def init_driver(request):
    global driver
    options = Options()
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    driver.implicitly_wait(5)
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)


@pytest.fixture(autouse=True)
def navigate_to_dview():
    driver.get(TestParams.BASE_URL)