import time

import pytest
from pages.demoqa import DemoQa
from pages.radio_page import Radio


@pytest.mark.skip
def test_decor_3(browser):
    demo = DemoQa(browser)
    demo.visit()
    demo.h5.check_count_elements(6)
    for element in demo.h5.find_elements():
        assert element.text != ''


@pytest.mark.skipif(True, reason='просто пропустить')
def test_decor_1(browser):
    radio = Radio(browser)
    radio.visit()

    radio.btn_yes.click_force()
    assert radio.text.get_text() == 'You have selected Yes'
    time.sleep(2)
    radio.btn_impressive.click_force()
    assert radio.text.get_text() == 'You have selected Impressive'
    time.sleep(2)
    assert 'disabled' in radio.btn_no.get_dom_attribute('class')


