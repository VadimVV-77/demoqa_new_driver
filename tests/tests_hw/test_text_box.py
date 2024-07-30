from pages.text_box_page import TextBox
import time


def test_text_box(browser):
    text_box = TextBox(browser)
    text_box.visit()
    text_box.name.send_keys('Junior')
    text_box.current_address.send_keys('Moscow')
    time.sleep(2)
    text_box.text_box_btn_submit.click_force()
    time.sleep(2)
    assert text_box.text_box_modal_dialog.get_text() == 'Name:Junior\nCurrent Address :Moscow'
    time.sleep(2)
    text_box.name.clear()    # * сравнение и ввод текста, реализовать через переменную
    text_box.current_address.clear()
    time.sleep(2)
    text_box.name.send_keys('Middle')
    text_box.current_address.send_keys('SPb')
    time.sleep(2)
    text_box.text_box_btn_submit.click_force()
    time.sleep(2)
    expected_text = 'Name:Middle\nCurrent Address :SPb'
    actual_text = text_box.text_box_modal_dialog.get_text()
    assert expected_text == actual_text
