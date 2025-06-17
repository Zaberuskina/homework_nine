from pages.registration_page import RegistrationPage
from data.student_data import student

def test_submit_registration_form():
    registration_page = RegistrationPage()

    registration_page.open() \
        .fill_first_name(student['first_name']) \
        .fill_last_name(student['last_name']) \
        .fill_email(student['email']) \
        .select_gender(student['gender']) \
        .fill_phone(student['phone']) \
        .set_birth_date(student['birth_month'], student['birth_year'], student['birth_day']) \
        .fill_subject(student['subject']) \
        .select_hobbies() \
        .upload_picture(student['picture']) \
        .fill_address(student['address']) \
        .select_state_and_city() \
        .submit()

    registration_page.should_have_registered(
        name=f"{student['first_name']} {student['last_name']}",
        email=student['email'],
        gender=student['gender'],
        phone=student['phone'],
        birth=f"{student['birth_day']} {student['birth_month']},{student['birth_year']}",
        subject=student['subject'],
        hobbies=student['hobbies'],
        picture=student['picture'],
        address=student['address'],
        state_and_city=student['state_and_city']
    )
