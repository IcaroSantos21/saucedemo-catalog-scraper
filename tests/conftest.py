import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page

@pytest.fixture
def inventory_page(driver, login_page):
    login_page.login('standard_user', 'secret_sauce')
    page = InventoryPage(driver)

    page.wait_for_products()
    return page


