import os
from selene.support.shared import browser
from selene import have

def test_registration_form():

    #must be filled
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Теодор')
    browser.element('#lastName').type('Вышеградский')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('8122051321')

    #optional
    browser.element('#userEmail').type('teodor@gmail.com')
    browser.element('#dateOfBirthInput').click()
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('#dateOfBirthInput').click()

    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="8"]' ).click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1992"]').click()
    browser.element('.react-datepicker__day--010').click()

    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').set_value(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'tests/6289.jpg')))
    browser.element('#currentAddress').type('Russia')

    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Merrut').press_enter()

    #submit
    browser.element('#submit').press_enter()

    browser.element('.table').should(have.text(
        'Теодор Вышеградский' and
        'teodor@gmail.com' and
        'Male' and
        '8122051321' and
        '10 September, 1992' and
        'Arts' and
        'Sports' and
        '6289.jpg' and
        'Russia' and
        'Uttar Pradesh Merrut'
    ))





