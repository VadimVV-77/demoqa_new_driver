import time

import pytest
from pages.alert import Alerts
from pages.accordion import Accordion
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQa


@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_attribute_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(4)

    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
    #assert page.viewport.get_dom_attribute('name') == 'viewport', f"Expected 'viewport', got {page.viewport.get_dom_attribute('name')}"