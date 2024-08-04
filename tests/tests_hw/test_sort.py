from pages.tables import Tables
import time





def test_sort_tables(browser):
    page_tables = Tables(browser)
    page_tables.visit()
    assert page_tables.equal_url()

    page_tables.colon_first_name.click()
    time.sleep(2)
    page_tables.colon_first_name.check_attribute_contains_part('class', 'sort')
    page_tables.colon_last_name.click()
    time.sleep(2)
    page_tables.colon_last_name.check_attribute_contains_part('class', 'sort')
    page_tables.colon_age.click()
    time.sleep(2)
    page_tables.colon_age.check_attribute_contains_part('class', 'sort')
    page_tables.colon_user_email.click()
    time.sleep(2)
    page_tables.colon_user_email.check_attribute_contains_part('class', 'sort')
    page_tables.colon_salary.click()
    time.sleep(2)
    page_tables.colon_salary.check_attribute_contains_part('class', 'sort')
    page_tables.colon_department.click()
    time.sleep(2)
    page_tables.colon_department.check_attribute_contains_part('class', 'sort')
