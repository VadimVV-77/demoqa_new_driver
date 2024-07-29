from pages.demoqa import DemoQa
from pages.books_page import BooksPage


def test_navigation(browser):
    demo_qa_page = DemoQa(browser)
    books_page = BooksPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_books.click()

    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert books_page.equal_url()
