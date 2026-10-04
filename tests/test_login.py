from Pages.homepage import Homepage
from Pages.loginpage_py import LoginPage
from playwright.sync_api import expect
from config import Config

def test_loginfunction(page):
    homepage = Homepage(page)
    loginpage = LoginPage(page)
    conf=Config()

    homepage.click_myaccount()
    homepage.click_login()
    page.wait_for_timeout(2000)
    loginpage.enter_email(conf.invalid_email)
    loginpage.enter_password(conf.invalid_password)
    loginpage.enter_submit()
