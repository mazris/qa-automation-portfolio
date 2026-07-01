import sys
import os

import allure
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from data.test_data import TestData

@pytest.mark.smoke
@allure.suite("Smoke Suite")
@allure.description("Verify that a valid user can login and is redirected to the products page")
def test_valid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login(
        TestData.STANDARD_USER['username'],
        TestData.STANDARD_USER['password']
    )
    page.wait_for_url("**/inventory.html")
    title = page.inner_text(".title")

    #assert condition, message_if_it_fails
    assert title == TestData.PRODUCTS_TITLE, f"Expected '{TestData.PRODUCTS_TITLE}' but got '{title}'"

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify that a invalid credebtials show the correct error message")
def test_invalid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login(
        TestData.INVALID_USER['username'],
        TestData.INVALID_USER['password']
    )
    assert login.is_error_visible(), "FAIL — error message not visible"
    error = login.get_error_message()
    assert error == TestData.LOGIN_ERROR, f"Expected '{TestData.LOGIN_ERROR}' but got '{error}'"

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify that a a locked out user see the correct error message")
def test_locked_user_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login(
        TestData.LOCKED_USER["username"],
        TestData.LOCKED_USER["password"]
    )
    assert login.is_error_visible(), "FAIL — error message not visible"
    error = login.get_error_message()
    assert error == TestData.LOCKED_ERROR, f"Expected '{TestData.LOCKED_ERROR}' but got '{error}'"



