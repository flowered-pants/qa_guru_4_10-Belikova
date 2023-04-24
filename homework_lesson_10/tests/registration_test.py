from homework_lesson_10.data.users import student
from homework_lesson_10.model.pages.registration_page_high_level import RegistrationPage



def test_registration_form(browser_managment):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)
