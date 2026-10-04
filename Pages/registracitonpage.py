from playwright.sync_api import Page


class RegistrationPage(Page):
    def __init__(self,page: Page):
        self.page = page
        self.text_firstname=page.locator("//input[@id='input-firstname']")
        self.text_lastname=page.locator("//input[@id='input-lastname']")
        self.text_email=page.locator("//input[@id='input-email']")
        self.text_phone=page.locator("//input[@id='input-telephone']")
        self.text_password=page.locator("//input[@id='input-password']")
        self.text_confirm=page.locator("//input[@id='input-confirm']")

        self.checbox=page.locator("//input[@name='agree']")
        self.btn_continue=page.locator("//input[@value='Continue']")


    def set_firstname(self,firstname):
        self.text_firstname.fill(firstname)

    def set_lastname(self,lastname):
        self.text_lastname.fill(lastname)

    def set_email(self,email):
        self.text_email.fill(email)

    def set_password(self,password):
        self.text_password.fill(password)
    def setphone(self,phone):
        self.text_phone.fill(phone)
    def reconfirimpassword(self,password):
        self.text_confirm.fill(password)

    def privacycheckbox(self):
        self.checbox.check()
    def submit(self):
        self.btn_continue.click()

    def perfrorm_register(self,use_data:dict):
        self.set_firstname(use_data['firstname'])
        self.set_lastname(use_data['lastname'])
        self.set_email(use_data['email'])
        self.set_password(use_data['password'])
        self.setphone(use_data['telephone'])
        self.reconfirimpassword(use_data['password'])
        self.privacycheckbox()
        self.btn_continue.click()
