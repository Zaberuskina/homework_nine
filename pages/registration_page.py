from selene import have, command
from selene.support.shared import browser
from pathlib import Path
from locators.registration_locators import RegistrationPageLocators as Locators

DATA_DIR = Path(__file__).parent.parent / 'data'

class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element(Locators.FIRST_NAME_INPUT).type(value)
        return self

    def fill_last_name(self, value):
        browser.element(Locators.LAST_NAME_INPUT).type(value)
        return self

    def fill_email(self, value):
        browser.element(Locators.EMAIL_INPUT).type(value)
        return self

    def select_gender(self, value):
        browser.element(Locators.GENDER_MALE_RADIO).click()
        return self

    def fill_phone(self, value):
        browser.element(Locators.PHONE_INPUT).type(value)
        return self

    def set_birth_date(self, month, year, day):
        browser.element(Locators.DATE_INPUT).click()
        browser.element(Locators.MONTH_SELECT).type(month)
        browser.element(Locators.YEAR_SELECT).type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, value):
        browser.element(Locators.SUBJECTS_INPUT).type(value).press_enter()
        return self

    def select_hobbies(self):
        browser.element(Locators.HOBBIES_SPORTS).perform(command.js.click)
        browser.element(Locators.HOBBIES_MUSIC).perform(command.js.click)
        return self

    def upload_picture(self, file_name):
        file_path = DATA_DIR / file_name
        if file_path.exists():
            browser.element(Locators.UPLOAD_PICTURE).set_value(str(file_path))
        return self

    def fill_address(self, value):
        browser.element(Locators.ADDRESS_INPUT).type(value)
        return self

    def select_state_and_city(self):
        browser.element(Locators.STATE_SELECT).perform(command.js.click)
        browser.element(Locators.STATE_OPTION).click()

        browser.element(Locators.CITY_SELECT).perform(command.js.click)
        browser.element(Locators.CITY_OPTION).click()
        return self

    def submit(self):
        browser.element(Locators.SUBMIT_BUTTON).perform(command.js.click)
        return self

    def should_have_registered(self, name, email, gender, phone, birth, subject, hobbies, picture, address, state_and_city):
        browser.element(Locators.MODAL_TITLE).should(have.text('Thanks for submitting the form'))
        browser.all(Locators.TABLE_ROWS).should(have.exact_texts(
            f'Student Name {name}',
            f'Student Email {email}',
            f'Gender {gender}',
            f'Mobile {phone}',
            f'Date of Birth {birth}',
            f'Subjects {subject}',
            f'Hobbies {hobbies}',
            f'Picture {picture}',
            f'Address {address}',
            f'State and City {state_and_city}'
        ))
        return self
