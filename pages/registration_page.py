from selene import browser, have, be, command, query
from locators.registration_locators import RegistrationPageLocators as Locators
from selene.support.shared.jquery_style import s, ss
from data.student_data import Student
import os


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("document.body.style.zoom='0.5'")
        return self

    def fill_first_name(self, value):
        s(Locators.FIRST_NAME_INPUT).type(value)
        return self

    def fill_last_name(self, value):
        s(Locators.LAST_NAME_INPUT).type(value)
        return self

    def fill_email(self, value):
        s(Locators.EMAIL_INPUT).type(value)
        return self

    def select_gender(self):
        s(Locators.GENDER_MALE_RADIO).click()
        return self

    def fill_phone(self, value):
        s(Locators.PHONE_INPUT).type(value)
        return self

    def select_birth_date(self, day, month, year):
        s(Locators.DATE_INPUT).click()
        s(Locators.MONTH_SELECT).type(month)
        s(Locators.YEAR_SELECT).type(year)
        s(f'.react-datepicker__day--0{day.zfill(2)}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_subject(self, value):
        s(Locators.SUBJECTS_INPUT).type(value).press_enter()
        return self

    def select_hobby(self):
        s(Locators.HOBBIES_SPORTS).click()
        return self

    def upload_picture(self, file_path):
        absolute_path = os.path.abspath(file_path)
        s(Locators.UPLOAD_PICTURE).type(absolute_path)
        return self

    def fill_address(self, value):
        s(Locators.ADDRESS_INPUT).type(value)
        return self

    def select_state(self, value):
        s(Locators.STATE_SELECT).perform(command.js.scroll_into_view).click()
        ss(Locators.STATE_OPTIONS).with_(timeout=6).should(have.size_greater_than(0))
        ss(Locators.STATE_OPTIONS).element_by(have.exact_text(value)).click()
        return self

    def select_city(self, value):
        s(Locators.CITY_SELECT).perform(command.js.scroll_into_view).click()
        ss(Locators.CITY_OPTIONS).with_(timeout=6).should(have.size_greater_than(0))
        ss(Locators.CITY_OPTIONS).element_by(have.exact_text(value)).click()
        return self

    def submit(self):
        s(Locators.SUBMIT_BUTTON).perform(command.js.click)
        return self

    def should_have_modal_title(self, value):
        s(Locators.MODAL_TITLE).should(have.text(value))
        return self

    def should_have_registered(self, student: Student):
        expected_values = [
            f'{student.first_name} {student.last_name}',
            student.email,
            student.gender,
            student.phone,
            f'{student.birth_day} {student.birth_month},{student.birth_year}',
            student.subject,
            'Sports',
            student.picture,
            student.address,
            f'{student.state} {student.city}'
        ]
        actual_values = [row.element('td:nth-child(2)').get(query.text) for row in ss(Locators.TABLE_ROWS)]
        assert actual_values == expected_values, f'\nОжидалось: {expected_values}\nФактически: {actual_values}'
        return self

    def register(self, student: Student):
        return self.fill_first_name(student.first_name) \
                   .fill_last_name(student.last_name) \
                   .fill_email(student.email) \
                   .select_gender() \
                   .fill_phone(student.phone) \
                   .select_birth_date(student.birth_day, student.birth_month, student.birth_year) \
                   .fill_subject(student.subject) \
                   .select_hobby() \
                   .upload_picture(f'data/{student.picture}') \
                   .fill_address(student.address) \
                   .select_state(student.state) \
                   .select_city(student.city) \
                   .submit()