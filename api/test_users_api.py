import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import allure
from api.api_client import APIClient

@pytest.fixture
def client():
    return APIClient()

@pytest.mark.smoke
@allure.suite("Smoke Suite")
@allure.description("Verify that a valid user can be retrieved successfully")
def test_get_valid_user(client):
    response = client.get_user(1)
    assert response.status_code == 200 , f"Expected 200 but got {response.status_code}"
    data = response.json()
    assert data["id"] == 1 , f"Expected {1} but got {data['id']}"
    assert "name" in data, "Response missing name field"
    assert "email" in data, "Response missing email field"
    print("PASS — valid user retrieved successfully")

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify that requesting a non-existent user returns 404")
def test_get_non_existent_user(client):
    response = client.get_user(999)
    assert response.status_code == 404, f"Expected 404 but got {response.status_code}"
    print("PASS — non-existent user returns 404")

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify that a new user can be created successfully")
def test_create_user(client):
    payload ={
        "name": "Sarah Johnson",
        "username": "sarahj",
        "email": "sarah@test.com"
    }

    response = client.create_user(payload)
    assert response.status_code == 201, f"Expected 201 but got {response.status_code}"

    data = response.json()
    assert data["name"] == "Sarah Johnson", f"Expected Sarah Johnson but got {data['name']}"
    assert "id" in data, "Response missing id field — user was not created"
    print(f"PASS — user created with id {data['id']}")

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify that an existing user can be updated successfully")
def test_update_user(client):

    payload = {
        "name": "Sarah Johnson Updated",
        "username": "sarahj",
        "email": "sarah_updated@test.com"
    }

    response = client.update_user(1,payload)

    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    data = response.json()
    assert data["name"] == "Sarah Johnson Updated", \
        f"Expected updated name but got {data['name']}"
    print("PASS — user updated successfully")

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify that a user can be deleted successfully")
def test_delete_user(client):

    response = client.delete_user(1)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    print("PASS — user deleted successfully")

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify that all users are returned correctly")
def test_get_all_users(client):
    response = client.get_all_users()
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    data = response.json()
    assert len(data) > 0, "Expected users list but got empty response"
    assert "name" in data[0], "First user missing name field"
    print(f"PASS — {len(data)} users returned successfully")


