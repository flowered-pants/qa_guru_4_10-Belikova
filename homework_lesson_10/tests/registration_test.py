from homework_lesson_10.data import users
from homework_lesson_10.data.users import Students
from homework_lesson_10.model.pages.registration_page_high_level import RegistrationPage

student = Students(first_name='Evgeniia', last_name='Belikova', email='mur@loc.ru',
                   gender='Female', number='88002000600', birthday='27 March,1997', subject='Computer Science',
                   hobbies='Sports, Reading, Music', picture='pic.png', address='Moscow, Russia',
                   state_and_city='Uttar Pradesh Merrut')

def test_registration_form(browser_managment):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)
