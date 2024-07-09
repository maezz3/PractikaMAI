import requests

BASE_URL = "https://virtserver.swaggerhub.com/slopetown/slopetownpetstore/1.0.0"


def create_pet_request(name, status):
    payload = {
        "name": name,
        "photoUrls": ["string"],
        "status": status
    }
    return requests.Request('POST', f"{BASE_URL}/pet", json=payload).prepare()


def update_pet_request(pet_id, name, status):
    payload = {
        "id": pet_id,
        "name": name,
        "photoUrls": ["string"],
        "status": status
    }
    return requests.Request('PUT', f"{BASE_URL}/pet", json=payload).prepare()


def find_pets_by_status_request(status):
    params = {"status": status}
    return requests.Request('GET', f"{BASE_URL}/pet/findByStatus", params=params).prepare()


def find_pets_by_tags_request(tags):
    params = {"tags": tags}
    return requests.Request('GET', f"{BASE_URL}/pet/findByTags", params=params).prepare()


def get_pet_by_id_request(pet_id):
    return requests.Request('GET', f"{BASE_URL}/pet/{pet_id}").prepare()


def update_pet_with_form_request(pet_id, name, status):
    data = {
        "name": name,
        "status": status
    }
    return requests.Request('POST', f"{BASE_URL}/pet/{pet_id}", data=data).prepare()


def delete_pet_request(pet_id):
    return requests.Request('DELETE', f"{BASE_URL}/pet/{pet_id}").prepare()


def upload_image_request(pet_id, file_path):
    files = {'file': open(file_path, 'rb')}
    return requests.Request('POST', f"{BASE_URL}/pet/{pet_id}/uploadImage", files=files).prepare()


def get_inventory_request():
    return requests.Request('GET', f"{BASE_URL}/store/inventory").prepare()


def place_order_request(order_id, pet_id, quantity, ship_date, status, complete):
    payload = {
        "id": order_id,
        "petId": pet_id,
        "quantity": quantity,
        "shipDate": ship_date,
        "status": status,
        "complete": complete
    }
    return requests.Request('POST', f"{BASE_URL}/store/order", json=payload).prepare()


def get_order_by_id_request(order_id):
    return requests.Request('GET', f"{BASE_URL}/store/order/{order_id}").prepare()


def delete_order_request(order_id):
    return requests.Request('DELETE', f"{BASE_URL}/store/order/{order_id}").prepare()


def create_user_request(user_id, username, first_name, last_name, email, password, phone, user_status):
    payload = {
        "user_id": user_id,
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": user_status
    }
    return requests.Request('POST', f"{BASE_URL}/user", json=payload).prepare()


def create_users_with_array_request(users):
    return requests.Request('POST', f"{BASE_URL}/user/createWithArray", json=users).prepare()


def create_users_with_list_request(users):
    return requests.Request('POST', f"{BASE_URL}/user/createWithList", json=users).prepare()


def login_user_request(username, password):
    params = {
        "username": username,
        "password": password
    }
    return requests.Request('GET', f"{BASE_URL}/user/login", params=params).prepare()


def logout_user_request():
    return requests.Request('GET', f"{BASE_URL}/user/logout").prepare()


def get_user_by_name_request(username):
    return requests.Request('GET', f"{BASE_URL}/user/{username}").prepare()


def update_user_request(user_id, username, first_name, last_name, email, password, phone, user_status):
    payload = {
        "user_id": user_id,
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": user_status
    }
    return requests.Request('PUT', f"{BASE_URL}/user/{username}", json=payload).prepare()


def delete_user_request(username):
    return requests.Request('DELETE', f"{BASE_URL}/user/{username}").prepare()
