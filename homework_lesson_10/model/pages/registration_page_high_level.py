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

    def register(self, student):
        browser.element('#firstName').should(be.blank).type(student.first_name)
        browser.element('#lastName').should(be.blank).type(student.last_name)
        browser.element('#userEmail').should(be.blank).type(student.email)
        browser.element('[for="gender-radio-2"]').should(be.clickable).click()
        browser.element('#userNumber').should(be.blank).type(student.number)
        browser.driver.execute_script('window.scrollBy(0, 300)')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'option[value="{student.year}"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'option[value="{student.month}"]').click()
        browser.element(f'.react-datepicker__day--0{student.day}').click()
        browser.element('#subjectsInput').click()
        browser.element('#subjectsInput').send_keys('Computer Science')
        browser.element('#subjectsInput').press(Keys.TAB)
        browser.element('[for="hobbies-checkbox-1"]').should(be.clickable).click()
        browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()
        browser.element('[for="hobbies-checkbox-3"]').should(be.clickable).click()
        browser.element('#uploadPicture').send_keys(resources.path())
        browser.element('#currentAddress').should(be.blank).type(student.address)
        browser.driver.execute_script('window.scrollBy(0, 500)')
        browser.element('#state').click()
        browser.element('#react-select-3-option-1').click()
        browser.element('#city').click()
        browser.element('#react-select-4-option-2').click()
        browser.element('#submit').click()

    def should_have_registered(self, student):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.exact_texts(student.first_name + ' ' + student.last_name,
                                                                         student.email, student.gender,
                                                                         student.number, student.day + ' February'
                                                                         + ',' + student.year, student.subject,
                                                                         student.hobbies, student.picture, student.address,
                                                                         student.state_and_city))
