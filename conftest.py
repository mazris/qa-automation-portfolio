import allure
import pytest
from playwright.sync_api import sync_playwright
from db.db_helper import DBHelper

def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: smoke test suite")
    config.addinivalue_line("markers", "regression: regression test suite")


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        #yield page is where the test runs
        yield page
        context.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )

@pytest.fixture(scope="function")
def db():
    helper = DBHelper()
    yield helper
    helper.reset_all_test_data()
    helper.disconnect()



