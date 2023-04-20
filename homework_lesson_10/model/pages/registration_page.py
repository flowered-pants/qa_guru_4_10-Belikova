from selene import browser
from selene import have, be
from selenium.webdriver.common.keys import Keys
from homework_lesson_10 import resources


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.should(have.title('DEMOQA'))
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')
        browser.element('.sidebar-content').execute_script('element.remove()')

    def type_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def type_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def type_email(self, mail):
        browser.element('#userEmail').should(be.blank).type(mail)

    def choose_gander(self):
        browser.element('[for="gender-radio-1"]').should(be.clickable)
        browser.element('[for="gender-radio-2"]').should(be.clickable).click()
        browser.element('[for="gender-radio-3"]').should(be.clickable)

    def type_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def type_birthday(self, year, month, day):
        browser.driver.execute_script('window.scrollBy(0, 300)')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'option[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'option[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def choose_subjects(self):
        browser.element('#subjectsInput').click()
        browser.element('#subjectsInput').send_keys('Computer Science')
        browser.element('#subjectsInput').press(Keys.TAB)

    def choose_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').should(be.clickable).click()
        browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()
        browser.element('[for="hobbies-checkbox-3"]').should(be.clickable).click()

    def choose_picture(self):
        browser.element('#uploadPicture').send_keys(resources.path())

    def type_address(self, address):
        browser.element('#currentAddress').should(be.blank).type(address)

    def choose_state_and_city(self):
        browser.driver.execute_script('window.scrollBy(0, 500)')
        browser.element('#state').click()
        browser.element('#react-select-3-option-1').click()
        browser.element('#city').click()
        browser.element('#react-select-4-option-2').click()

    def submit(self):
        browser.element('#submit').click()

    def assert_registration_user_data(self, full_name, email, gender, number, birthday,
                                      subject, hobbie, picture, address, state_and_city):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.exact_texts(
            full_name,
            email,
            gender,
            number,
            birthday,
            subject,
            hobbie,
            picture,
            address,
            state_and_city))

