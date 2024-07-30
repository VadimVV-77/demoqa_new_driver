
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from pages.books_page import BooksPage


def test_check_test_footer(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.footer.get_text()
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'



def test_check_test_central(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click_force()
    elements_page.central.get_text()
    assert elements_page.central.get_text() == 'Please select an item from left to start practice.'


def test_check_test_footer_books(browser):

    demo_qa_page = DemoQa(browser)
    books_page = BooksPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_books.click()
    books_page.footer.get_text()
    expected_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    actual_text = books_page.footer.get_text()
    assert expected_text, actual_text


def teste_page_elements(browser):
    el_page = ElementsPage(browser)

    el_page.visit()

    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()
    assert el_page.text_elements.get_text() == 'Please select an item from left to start practice.'
