from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')

        self.btn_delete_row = WebElement(driver, '[id^="delete-record"]')

        self.btn_add = WebElement(driver, '#addNewRecordButton')

        self.btn_submit = WebElement(driver, '#submit')

        self.btn_pen = WebElement(driver, '#edit-record-4 > svg')

        self.btn_delete_row_4 = WebElement(driver, '#delete-record-4 > svg')

        self.dialog_form = WebElement(driver, 'body > div.fade.modal.show > div > div')

        self.first_name = WebElement(driver, '#firstName')

        self.last_name = WebElement(driver, '#lastName')

        self.user_email = WebElement(driver, '#userEmail')

        self.age = WebElement(driver, '#age')

        self.salary = WebElement(driver, '#salary')

        self.department = WebElement(driver, '#department')

        self.row_4 = WebElement(driver, '.web-tables-wrapper .ReactTable .rt-tbody > div:nth-child(4)')
