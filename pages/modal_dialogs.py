from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_primary = WebElement(driver, '#modalWrapper > div>button')

        self.icon_main = WebElement(driver, '#app > header > a > img')

        self.btn_large = WebElement(driver, '#showLargeModal')

        self.btn_small = WebElement(driver, '#showSmallModal')

        self.small_close = WebElement(driver, '#closeSmallModal')

        self.large_close = WebElement(driver, '#closeLargeModal')

        self.small_modal = WebElement(driver, 'body > div.fade.modal.show > div > div')

        self.large_modal = WebElement(driver, 'body > div.fade.modal.show > div > div')
