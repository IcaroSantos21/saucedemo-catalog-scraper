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
def inventory_page(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    page = InventoryPage(driver)
    page.wait_for_products()
    return page


