import pytest
from utilities.apis import APIS
import uuid


@pytest.fixture(scope="module")
def apis():
    return APIS()

def test_getuser_validation(apis):
    response = apis.get("users")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_createuser_validation(apis,load_user_data):
    # user_data = {
    #     "name": "TestName",
    #     "username": "QA User",
    #     "email": "test@gmail.com"
    # }

    user_data = load_user_data["new user"]

    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data["email"] = unique_email

    response = apis.post("users",user_data)
    print(response.json())
    assert response.status_code == 201
    # assert response.json() ["name"] == "TestName"
    id = response.json()["id"]
    responseget = apis.get("users/10")
    print(responseget.json())
    assert responseget.status_code == 200
    assert responseget.json() ["name"] == "Clementina DuBuque"

def test_updateuser_validation(apis):
    user_data = {
    "name": "TestName T",
    "username": "QA User",
    "email": "test@gmail.com"
    }
    response = apis.put("users/1", user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["name"] == "TestName T"

def test_delete_users(apis):
    response = apis.delete("users/1", {})
    print(response.json())
    assert response.status_code == 200

