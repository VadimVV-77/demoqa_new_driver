import pytest
from selenium import webdriver
import logging


@pytest.fixture(scope="session")
def browser():
    logging.basicConfig(level=logging.DEBUG)
    driver = webdriver.Chrome()
    #driver.get("http://example.com")
    driver.set_window_size(1000, 1000)
    yield driver
    driver.quit()
