from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert accordion_page.section_content.visible()
    accordion_page.section_heading.click()
    time.sleep(2)
    assert not accordion_page.section_content.visible()


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert not accordion_page.section_2_content_child_1.visible()
    assert not accordion_page.section_2_content_child_2.visible()
    assert not accordion_page.section_3_content.visible()
