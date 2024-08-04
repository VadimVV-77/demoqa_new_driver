from pages.alert import Alerts
import time


def test_check_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert alert_page.equal_url()

    assert alert_page.time_alertButton.exist()
    assert not alert_page.alert()

    alert_page.time_alertButton.click()
    time.sleep(5)
    assert alert_page.alert()
    time.sleep(2)
    alert_page.alert().accept()
