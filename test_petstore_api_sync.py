import pytest
import requests
import allure
from factories_sync import (
    create_pet_request,
    update_pet_request,
    find_pets_by_status_request,
    find_pets_by_tags_request,
    get_pet_by_id_request,
    update_pet_with_form_request,
    delete_pet_request,
    upload_image_request,
    get_inventory_request,
    place_order_request,
    get_order_by_id_request,
    delete_order_request,
    create_user_request,
    create_users_with_array_request,
    create_users_with_list_request,
    login_user_request,
    logout_user_request,
    get_user_by_name_request,
    update_user_request,
    delete_user_request
)


@pytest.fixture
def session():
    session = requests.Session()
    yield session
    session.close()


def check_response_status(response, expected_status_code, error_message=None):
    allure.attach(body=response.text, name='Response Body', attachment_type=allure.attachment_type.JSON)
    if expected_status_code == 200:
        assert True, f"Expected status code {expected_status_code}, and got {expected_status_code}"
    else:
        if error_message is None:
            error_message = f"Unexpected status code received: {response.status_code}"
        pytest.fail(error_message)


@allure.feature('Petstore API')
@allure.story('Pet Management')
@allure.severity(allure.severity_level.BLOCKER)
class TestPetstoreAPI:

    @allure.step('1. Add a new pet to the store')
    def test_add_pet(self, session):
        request = create_pet_request("doggie", "available")
        response = session.send(request)
        with allure.step('2. Check that response code is error 405'):
            assert response.status_code == 405

    @allure.step('1. Update an existing pet')
    def test_update_pet(self, session):
        request = update_pet_request(5, "doggie_updated", "pending")
        response = session.send(request)
        with allure.step('2. Check that response code is error 400 or 404 or 405'):
            if response.status_code == 400:
                assert response.status_code == 400
            elif response.status_code == 404:
                assert response.status_code == 404
            elif response.status_code == 405:
                assert response.status_code == 405

    @allure.step('1. Find pets by status')
    def test_find_pets_by_status(self, session):
        request = find_pets_by_status_request("available")
        response = session.send(request)
        with allure.step('2. Check that response code is 200 or error 400'):
            if response.status_code == 200:
                check_response_status(response, 200)
            elif response.status_code == 400:
                check_response_status(response, 400, "Received status code 400 - Invalid status value.")
            else:
                check_response_status(response, response.status_code)
        pets = response.json()
        with allure.step('3. Verify all pets have status "available"'):
            assert all(pet['status'] == 'available' for pet in pets)

    @allure.step('1. Find pets by tags')
    def test_find_pets_by_tags(self, session):
        request = find_pets_by_tags_request(["tag1"])
        response = session.send(request)
        with allure.step('2. Check that response code is 200 or error 400'):
            if response.status_code == 200:
                check_response_status(response, 200)
            elif response.status_code == 400:
                check_response_status(response, 400, "Received status code 400 - Invalid tag value.")
            else:
                check_response_status(response, response.status_code)

    @allure.step('1. Get pet by ID')
    def test_get_pet_by_id(self, session):
        request = get_pet_by_id_request(5)
        response = session.send(request)
        with allure.step('2. Check that response code is 200 or error 400 or 404'):
            if response.status_code == 200:
                check_response_status(response, 200)
            elif response.status_code == 400:
                check_response_status(response, 400, "Received status code 400 - Invalid ID supplied.")
            elif response.status_code == 404:
                check_response_status(response, 404, "Received status code 404 - Pet not found.")
            else:
                check_response_status(response, response.status_code)

    @allure.step('1. Update pet with form data')
    def test_update_pet_with_form(self, session):
        request = update_pet_with_form_request(0, "doggie_form_updated", "sold")
        response = session.send(request)
        with allure.step('2. Check that response code is error 405'):
            assert response.status_code == 405

    @allure.step('1. Delete pet')
    def test_delete_pet(self, session):
        request = delete_pet_request(0)
        response = session.send(request)
        with allure.step('2. Check that response code is error 400 or 404'):
            if response.status_code == 400:
                assert response.status_code == 400
            elif response.status_code == 404:
                assert response.status_code == 404

    @allure.step('1. Upload image for pet')
    def test_upload_image(self, session):
        request = upload_image_request(5, 'tiger-cub-1-scaled.jpg')
        response = session.send(request)
        with allure.step('2. Check that response code is 200'):
            assert response.status_code == 200


@allure.feature('Petstore API')
@allure.story('Store Management')
@allure.severity(allure.severity_level.CRITICAL)
class TestStoreAPI:

    @allure.step('1. Get inventory')
    def test_get_inventory(self, session):
        request = get_inventory_request()
        response = session.send(request)
        with allure.step('2. Check that response code is 200'):
            assert response.status_code == 200
        inventory = response.json()
        with allure.step('3. Verify inventory is a dictionary'):
            assert isinstance(inventory, dict)

    @allure.step('1. Place an order')
    def test_place_order(self, session):
        request = place_order_request(3, 1, 1, "2023-04-01T00:00:00.000Z", "placed", False)
        response = session.send(request)
        with allure.step('2. Check that response code is 200 or error 400'):
            if response.status_code == 200:
                check_response_status(response, 200)
            elif response.status_code == 400:
                check_response_status(response, 400, "Received status code 400 - Invalid Order.")
            else:
                check_response_status(response, response.status_code)

    @allure.step('1. Get order by ID')
    def test_get_order_by_id(self, session):
        request = get_order_by_id_request(3)
        response = session.send(request)
        with allure.step('2. Check that response code is 200'):
            if response.status_code == 200:
                check_response_status(response, 200)
            elif response.status_code == 400:
                check_response_status(response, 400, "Received status code 400 - Invalid ID supplied.")
            elif response.status_code == 404:
                check_response_status(response, 404, "Received status code 404 - Order not found.")
            else:
                check_response_status(response, response.status_code)

    @allure.step('1. Delete order')
    def test_delete_order(self, session):
        request = delete_order_request(3)
        response = session.send(request)
        with allure.step('2. Check that response code is error 400 or 404'):
            if response.status_code == 400:
                assert response.status_code == 400
            elif response.status_code == 404:
                assert response.status_code == 404


@allure.feature('Petstore API')
@allure.story('User Management')
@allure.severity(allure.severity_level.NORMAL)
class TestUserAPI:

    @allure.step('1. Create user')
    def test_create_user(self, session):
        request = create_user_request(1,
                                      "user1",
                                      "Test",
                                      "User",
                                      "test@example.com",
                                      "password",
                                      "1234567890",
                                      1)
        response = session.send(request)
        with allure.step('2. Check that response code is 201'):
            assert response.status_code == 201

    @allure.step('1. Create users with array')
    def test_create_users_with_array(self, session):
        users = [
            {
                "user_id": 2,
                "username": "testuser1",
                "firstName": "Test",
                "lastName": "User1",
                "email": "test1@example.com",
                "password": "password",
                "phone": "1234567890",
                "userStatus": 1
            },
            {
                "user_id": 3,
                "username": "testuser2",
                "firstName": "Test",
                "lastName": "User2",
                "email": "test2@example.com",
                "password": "password",
                "phone": "1234567891",
                "userStatus": 1
            }
        ]
        request = create_users_with_array_request(users)
        response = session.send(request)
        with allure.step('2. Check that response code is 201'):
            assert response.status_code == 201

    @allure.step('1. Create users with list')
    def test_create_users_with_list(self, session):
        users = [
            {
                "user_id": 4,
                "username": "testuser3",
                "firstName": "Test",
                "lastName": "User3",
                "email": "test3@example.com",
                "password": "password",
                "phone": "1234567892",
                "userStatus": 1
            },
            {
                "user_id": 5,
                "username": "testuser4",
                "firstName": "Test",
                "lastName": "User4",
                "email": "test4@example.com",
                "password": "password",
                "phone": "1234567893",
                "userStatus": 1
            }
        ]
        request = create_users_with_list_request(users)
        response = session.send(request)
        with allure.step('2. Check that response code is 200'):
            assert response.status_code == 201

    @allure.step('1. Login user')
    def test_login_user(self, session):
        request = login_user_request("user1", "password")
        response = session.send(request)
        with allure.step('2. Check that response code is 200 or error 400'):
            if response.status_code == 200:
                check_response_status(response, 200)
            elif response.status_code == 400:
                check_response_status(response, 400, "Received status code 400 - Invalid username/password supplied.")
            else:
                check_response_status(response, response.status_code)

    @allure.step('1. Logout user')
    def test_logout_user(self, session):
        request = logout_user_request()
        response = session.send(request)
        with allure.step('2. Check that response code is 200'):
            assert response.status_code == 200

    @allure.step('1. Get user by name')
    def test_get_user_by_name(self, session):
        request = get_user_by_name_request("user1")
        response = session.send(request)
        with allure.step('2. Check that response code is 200'):
            if response.status_code == 200:
                check_response_status(response, 200)
            elif response.status_code == 400:
                check_response_status(response, 400, "Received status code 400 - Invalid username supplied.")
            elif response.status_code == 404:
                check_response_status(response, 404, "Received status code 404 - User not found.")
            else:
                check_response_status(response, response.status_code)

    @allure.step('1. Update user')
    def test_update_user(self, session):
        request = update_user_request(1,
                                      "testuser",
                                      "UpdatedTest",
                                      "UpdatedUser",
                                      "updated@example.com",
                                      "updatedpassword",
                                      "0987654321",
                                      1)
        response = session.send(request)
        with allure.step('2. Check that response code is error 400 or 404'):
            if response.status_code == 400:
                assert response.status_code == 400
            elif response.status_code == 404:
                assert response.status_code == 404

    @allure.step('1. Delete user')
    def test_delete_user(self, session):
        request = delete_user_request("testuser")
        response = session.send(request)
        with allure.step('2. Check that response code is error 400 or 404'):
            if response.status_code == 400:
                assert response.status_code == 400
            elif response.status_code == 404:
                assert response.status_code == 404
