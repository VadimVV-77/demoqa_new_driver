import time

from pages.progress_bar_page import ProgressBar


def test_progress_bar(browser):
    page_bar = ProgressBar(browser)
    page_bar.visit()
    time.sleep(2)

    page_bar.btn_Bar.click()

    while True:
        if page_bar.progressBar.get_dom_attribute('aria-valuenow') == '51':
            page_bar.btn_Bar.click()
            break
    time.sleep(2)
