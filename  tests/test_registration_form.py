from pages.registration_page import RegistrationPage
from data.student_data import Student

def test_submit_registration_form():
    registration_page = RegistrationPage()
    student = Student()

    registration_page.open() \
        .register(student) \
        .should_have_registered(student)
