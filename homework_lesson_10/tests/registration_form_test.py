from homework_lesson_10.model.pages.registration_page import RegistrationPage


def test_registration_form(browser_managment):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.type_first_name('Evgeniia')
    registration_page.type_last_name('Belikova')
    registration_page.type_email('mur@loc.ru')
    registration_page.choose_gander()
    registration_page.type_number('88002000600')
    registration_page.type_birthday('1997','3','31')
    registration_page.choose_subjects()
    registration_page.choose_hobbies()
    registration_page.choose_picture()
    registration_page.type_address('Moscow, Russia')
    registration_page.choose_state_and_city()
    registration_page.submit()
    registration_page.assert_registration_user_data(
            'Evgeniia Belikova',
            'mur@loc.ru',
            'Female',
            '8800200060',
            '31 March,1997',
            'Computer Science',
            'Sports, Reading, Music',
            'pic.png',
            'Moscow, Russia',
            'Uttar Pradesh Merrut')
