import pytest
from pages.modal_dialogs import ModalDialogs
import time


def is_page_accessible(browser):
    try:
        browser.get(browser.current_url)
        return True
    except Exception:
        return False


@pytest.mark.skipif(not is_page_accessible, reason="Page is not accessible")
def test_check_modal(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()
    assert modal_dialogs.equal_url()
    assert modal_dialogs.btns_primary.check_count_elements(count=2)
    assert modal_dialogs.btn_large.exist()
    assert modal_dialogs.btn_small.exist()
    modal_dialogs.btn_small.click()
    time.sleep(2)
    assert modal_dialogs.small_modal.exist()
    assert modal_dialogs.small_close.exist()
    modal_dialogs.small_close.click()
    time.sleep(2)
    assert not modal_dialogs.small_modal.exist()
    modal_dialogs.btn_large.click()
    time.sleep(2)
    assert modal_dialogs.large_modal.exist()
    assert modal_dialogs.large_close.exist()
    modal_dialogs.large_close.click()
    time.sleep(2)
    assert not modal_dialogs.large_modal.exist()
