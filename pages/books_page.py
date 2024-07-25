from pages.base_page import BasePage
from components.components import WebElement


class BooksPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/books'
        super().__init__(driver, self.base_url)
        self.footer = WebElement(driver, '#app > footer')
