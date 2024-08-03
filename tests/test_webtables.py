from pages.tables import Tables
import time


def test_tables(browser):
    page_tables = Tables(browser)
    page_tables.visit()
    assert not page_tables.no_data.exist()

    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click_force()

    time.sleep(2)
    assert page_tables.no_data.exist()


def test_tables_case(browser):
    page_tables = Tables(browser)
    page_tables.visit()
    assert page_tables.btn_add.exist()
    page_tables.btn_add.click()
    time.sleep(2)
    assert page_tables.dialog_form.exist()
    page_tables.btn_submit.click()
    time.sleep(2)
    page_tables.first_name.send_keys('tester')
    page_tables.last_name.send_keys('testerovich')
    page_tables.user_email.send_keys('test@ttt.tt')
    page_tables.age.send_keys('34')
    page_tables.salary.send_keys('100000')
    page_tables.department.send_keys('QA')
    time.sleep(2)
    page_tables.btn_submit.click()
    time.sleep(2)
    assert not page_tables.dialog_form.exist()
    expected_text = 'tester\ntesterovich\n34\ntest@ttt.tt\n100000\nQA'
    assert page_tables.row_4.get_text().strip() == expected_text.strip()
    page_tables.btn_pen.click()
    time.sleep(2)
    assert page_tables.dialog_form.exist()
    assert page_tables.first_name.get_dom_attribute('value') == 'tester'
    assert page_tables.last_name.get_dom_attribute('value') == 'testerovich'
    assert page_tables.user_email.get_dom_attribute('value') == 'test@ttt.tt'
    assert page_tables.age.get_dom_attribute('value') == '34'
    assert page_tables.salary.get_dom_attribute('value') == '100000'
    assert page_tables.department.get_dom_attribute('value') == 'QA'
    time.sleep(2)
    page_tables.first_name.clear()
    time.sleep(2)
    page_tables.first_name.send_keys('Junior')
    time.sleep(2)
    page_tables.btn_submit.click()
    time.sleep(2)
    assert not page_tables.row_4.get_text().strip() == expected_text.strip()
    time.sleep(2)
    page_tables.btn_delete_row_4.click()
    time.sleep(2)
    assert page_tables.row_4.get_text().strip() == ''
