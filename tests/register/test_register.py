import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.chrome.options import Options



URL = "http://localhost:3000/react-shop"

fake = Faker()

def open_register_page(driver):
    button_register = driver.find_element(By.ID, "register-link")
    button_register.click()


def regsiter(driver, email=None, password_1=None, password_2=None):
    if email is None:
        email = fake.email()
    if password_1 is None:
        password_1 = fake.password()
        password_2 = password_1
    input_email = driver.find_element(By.ID, "name")
    input_password = driver.find_element(By.ID, "password1")
    input_password_2 = driver.find_element(By.ID, "password2")
    button_register = driver.find_element(By.ID, "register")
    input_email.send_keys(email)
    password = fake.password()
    input_password.send_keys(password_1)
    input_password_2.send_keys(password_2)
    button_register.click()

def get_toast_text(driver):
    toast = driver.find_element(By.ID, "toast-container")
    return toast.text


def get_error(driver, invalid_email):
    email_error = driver.find_element(By.CLASS_NAME, "card-panel")
    return email_error.text

@pytest.mark.xfail
def test_register_with_valid_data():
    # driver
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(20)
    driver.get("http://localhost:3000/react-shop")
    # register
    open_register_page(driver)
    # register window
    regsiter(driver)
    # assert
    assert get_toast_text(driver) == 'Success'
    driver.quit()

def test_register_invalid_email(invalid_email = 'test@test'):
    # driver
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(20)
    driver.get("http://localhost:3000/react-shop")
    # register
    open_register_page(driver)
    # register window
    invalid_email = 'test@test'
    regsiter(driver, email=invalid_email)
    # assert
    assert get_error(driver, invalid_email) == f'Error, {invalid_email} is not email address!'
    driver.quit()


    # # driver
    # driver = webdriver.Chrome()
    # driver.implicitly_wait(20)
    # driver.get("http://localhost:3000/react-shop")
    # # register
    # button_register = driver.find_element(By.ID, "register-link")
    # button_register.click()
    # # register window
    # input_email = driver.find_element(By.ID, "name")
    # input_password = driver.find_element(By.ID, "password1")
    # input_password_2 = driver.find_element(By.ID, "password2")
    # button_register = driver.find_element(By.ID, "register")
    # input_email.send_keys(invalid_email)
    # input_password.send_keys('Password1138')
    # input_password_2.send_keys('Password1138')
    # button_register.click()
    # # assert
    # email_error = driver.find_element(By.CLASS_NAME, "card-panel")
    # assert email_error.text == f'Error, {invalid_email} is not email address!'
    # driver.quit()

def test_register_invalid_password():
    pass