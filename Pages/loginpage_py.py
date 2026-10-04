from playwright.sync_api import Page
class LoginPage:
    def __init__(self,page: Page):
        self.page = page
        self.input_email=page.locator("//input[@id='input-email']")
        self.input_password=page.locator("//input[@id='input-password']")
        self.btn_sumit=page.locator('input[type="submit"]')
        self.warnign_message=page.locator(".alert.alert-danger.alert-dismissible")

    def enter_email(self,email):
        try:
            self.input_email.fill(email)
        except Exception as e:
            print(e)
        raise
    def enter_password(self,password):
        try:
            self.input_password.fill(password)
        except Exception as e:
            print(e)
    def enter_submit(self,submit):
        try:
            self.btn_sumit.click()
        except Exception as e:
            print(e)

    def login(self,email,password):
        self.enter_emai(email)
        self.enter_password(password)
        self.enter_submit

    def get_loginerrormessage(self):
        try:
            return self.warnign_message
        except Exception as e:
            print(e)
            return None