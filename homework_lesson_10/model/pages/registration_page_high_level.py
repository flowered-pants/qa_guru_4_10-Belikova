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

    def register(self, first_name, last_name, mail, gender, number, year, month, day, address):
        browser.element('#firstName').should(be.blank).type(first_name)
        browser.element('#lastName').should(be.blank).type(last_name)
        browser.element('#userEmail').should(be.blank).type(mail)
        browser.element('[for="gender-radio-2"]').should(be.clickable).click()
        browser.element('#userNumber').should(be.blank).type(number)
        browser.driver.execute_script('window.scrollBy(0, 300)')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'option[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'option[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        browser.element('#subjectsInput').click()
        browser.element('#subjectsInput').send_keys('Computer Science')
        browser.element('#subjectsInput').press(Keys.TAB)
        browser.element('[for="hobbies-checkbox-1"]').should(be.clickable).click()
        browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()
        browser.element('[for="hobbies-checkbox-3"]').should(be.clickable).click()
        browser.element('#uploadPicture').send_keys(resources.path())
        browser.element('#currentAddress').should(be.blank).type(address)
        browser.driver.execute_script('window.scrollBy(0, 500)')
        browser.element('#state').click()
        browser.element('#react-select-3-option-1').click()
        browser.element('#city').click()
        browser.element('#react-select-4-option-2').click()
        browser.element('#submit').click()

    def should_have_registered(self, first_name, last_name, email, gender, number, birthday,
                                      subject, hobbies, picture, address, state_and_city):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.exact_texts(first_name, last_name, email, gender, number,
                                                                         birthday, subject, hobbies, picture,
                                                                         address, state_and_city))

