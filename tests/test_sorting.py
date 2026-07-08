import sys
import os

import allure
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from data.test_data import TestData
from pages.inventory_page import InventoryPage

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify default page load sorts by names from A to Z")
def test_default_page_load_sorts_by_names(logged_in_page):

    # assert default sort option
    inventory = InventoryPage(logged_in_page)
    default_option = inventory.get_active_sort_options()
    assert default_option == TestData.SORT_DEFAULT, f"Expected '{TestData.SORT_DEFAULT}' but got '{default_option}'"

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify select Name A to Z sorts by names from A to Z")
def test_select_name_a_to_z(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    inventory.sort_by(inventory.get_sort_option_value_from_name(TestData.SORT_ATOZ))

    #assert sort option
    sort_option = inventory.get_active_sort_options()
    assert sort_option == TestData.SORT_ATOZ, f"Expected '{TestData.SORT_ATOZ}' but got '{sort_option}'"

    #assert first item name
    name = inventory.get_all_item_names()[0]
    assert name == TestData.SORT_FIRST_NAME_AZ, f"Expected '{TestData.SORT_FIRST_NAME_AZ}' but got '{name}'"

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify select Name Z to A sorts by names from Z to A")
def test_select_name_z_to_a(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    inventory.sort_by(inventory.get_sort_option_value_from_name(TestData.SORT_ZTOA))

    #assert sort option
    sort_option = inventory.get_active_sort_options()
    assert sort_option == TestData.SORT_ZTOA, f"Expected '{TestData.SORT_ZTOA}' but got '{sort_option}'"

    #assert first item name
    name = inventory.get_all_item_names()[0]
    assert name == TestData.SORT_FIRST_NAME_ZA, f"Expected '{TestData.SORT_FIRST_NAME_ZA}' but got '{name}'"

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify select price low to high sorts by price low to high")
def test_select_price_low_to_high(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    inventory.sort_by(inventory.get_sort_option_value_from_name(TestData.SORT_PRICE_LOWTOHIGH))

    #assert sort option
    sort_option = inventory.get_active_sort_options()
    assert sort_option == TestData.SORT_PRICE_LOWTOHIGH, f"Expected '{TestData.SORT_PRICE_LOWTOHIGH}' but got '{sort_option}'"

    #assert first item price
    price = inventory.get_all_item_prices()[0]
    assert price == TestData.SORT_LOWEST_PRICE, f"Expected '{TestData.SORT_LOWEST_PRICE}' but got '{price}'"


@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify select price high to low sorts by price high to low")
def test_select_price_high_to_low(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    inventory.sort_by(inventory.get_sort_option_value_from_name(TestData.SORT_PRICE_HIGHTOLOW))

    #assert sort option
    sort_option = inventory.get_active_sort_options()
    assert sort_option == TestData.SORT_PRICE_HIGHTOLOW, f"Expected '{TestData.SORT_PRICE_HIGHTOLOW}' but got '{sort_option}'"

    #assert first item price
    price = inventory.get_all_item_prices()[0]
    assert price == TestData.SORT_HIGHEST_PRICE, f"Expected '{TestData.SORT_HIGHEST_PRICE}' but got '{price}'"
