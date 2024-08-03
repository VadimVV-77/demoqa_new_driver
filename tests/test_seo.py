import time

import pytest
from pages.alert import Alerts
from pages.accordion import Accordion
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQa


# def test_check_title_demo(browser):
#     demo_qa_page = DemoQa(browser)
#     demo_qa_page.visit()
#     assert browser.title == 'DEMOQA'


@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(4)

    assert page.get_title() == 'DEMOQA'
