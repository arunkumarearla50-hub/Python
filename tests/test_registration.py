from Pages.homepage import Homepage
from Pages.registracitonpage import RegistrationPage
from utilities.random_data_util import RandomDataUtil

def test_registration(page):
    hp=Homepage(page)
    rp=RegistrationPage(page)
    ru=RandomDataUtil()
    password=ru.get_password()

    hp.click_myaccount()
    hp.click_registration()
    rp.set_firstname(ru.get_first_name())
    rp.set_lastname(ru.get_last_name())
    rp.set_email(ru.get_email())
    rp.set_password(password)
    rp.reconfirimpassword(password)

    rp.privacycheckbox()
    rp.submit()