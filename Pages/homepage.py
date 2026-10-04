from playwright.sync_api import Page
class Homepage:
    def __init__(self, page: Page):
        self.page = page
        self.link_myaccount=page.locator("span:has-text('My Account')")
        self.link_Registration=page.locator("//a[normalize-space()='Register']")
        self.link_Login=page.locator("span:has-text('Login')")
        self.serach_textbox=page.locator("// input[ @ name = 'search']")
        self.serach_link=page.locator("//button[@class='btn btn-default btn-lg']")

    def get_homepagetitle(self)->str:
        title=self.page.title()
        return title

    def click_myaccount(self):
        try:
            self.link_myaccount.click()
        except Exception as e:
            print("exeception while clicking the account",e)
            raise

    def click_registration(self):
        try:
            self.link_Registration.click()
        except Exception as e:
            print("exeception while clicking the account",e)
            raise
    def click_login(self):
        try:
            self.link_Login.click()
        except Exception as e:
            print("exeception while clicking the account",e)
            raise
    def click_serach_textbox(self):
        try:
            self.serach_textbox.click()
        except Exception as e:
            print("exeception while clicking the account",e)
    def click_serach_link(self):
        try:
            self.serach_link.click()
        except Exception as e:
            print("exeception while clicking the account",e)
            raise

