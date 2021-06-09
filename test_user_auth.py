import pytest
import random
import requests
import string


def generate_random_string(string_length):
    letters = string.printable
    random_string = ''.join(random.choice(letters) for i in range(string_length))
    return random_string


SUCCESSFUL_CREATED_USERNAME_TEMPLATE = generate_random_string(12)

USERNAME_SPEC_SYMBOLS_TEMPLATE = string.printable[62:]

PASSWORD_TEMPLATE = generate_random_string(21)

"""
User data for TestCaseUserCreate
"""

invalid_json = "{'a': 'b'}"'

SUCCESSFUL_REGISTRATION_DATA = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:15]
}

USER_DATA_WITHOUT_USERNAME = {
    "username": "",
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": PASSWORD_TEMPLATE[:15]
}

USER_DATA_WITHOUT_PASSWORD = {
    "username": generate_random_string(12),
    "password1": "",
    "password2": ""
}

USER_DATA_TOO_LONG_USERNAME = {
  "username": generate_random_string(51),
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:15]
}

USER_DATA_TOO_LONG_PASSWORD = {
  "username": generate_random_string(12),
  "password1": PASSWORD_TEMPLATE[:21],
  "password2": PASSWORD_TEMPLATE[:21]
}

USER_DATA_USERNAME_WITH_SPECIAL_SYMBOLS = {
    "username": USERNAME_SPEC_SYMBOLS_TEMPLATE,
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": PASSWORD_TEMPLATE[:15]
}

USER_DATA_NOT_EQUAL_PASSWORDS = {
  "username": generate_random_string(12),
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:16]
}

USER_DATA_SHORT_PASSWORD = {
    "username": generate_random_string(12),
    "password1": PASSWORD_TEMPLATE[:5],
    "password2": PASSWORD_TEMPLATE[:5]
}

USER_DATA_MIN_LENGTH_PASSWORD = {
    "username": generate_random_string(12),
    "password1": PASSWORD_TEMPLATE[:6],
    "password2": PASSWORD_TEMPLATE[:6]
}

USER_DATA_SHORT_USERNAME = {
    "username": generate_random_string(5),
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": PASSWORD_TEMPLATE[:15]
}

USER_DATA_USERNAME_STARTED_WITH_WHITESPACE = {
    "username": " " + generate_random_string(12),
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": PASSWORD_TEMPLATE[:15]
}

"""
User data for TestCaseUserPasswordReplace
"""

SUCCESSFUL_PASSWORD_REPLACE_DATA = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "old_password": PASSWORD_TEMPLATE[:15],
  "password1": PASSWORD_TEMPLATE[3:21],
  "password2": PASSWORD_TEMPLATE[3:21]
}

SUCCESSFUL_PASSWORD_REPLACE_DATA_WITH_NEW_PASSWORD = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "old_password": PASSWORD_TEMPLATE[3:21],
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:15]
}

USER_DATA_INCORRECT_OLD_PASSWORD = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "old_password": PASSWORD_TEMPLATE[:17],
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:15]
}

USER_DATA_NEW_PASSWORDS_ARE_NOT_EQUAL = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "old_password": PASSWORD_TEMPLATE[3:21],
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:17]
}

USER_DATA_NEW_PASSWORDS_ARE_NOT_EQUAL_2 = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "old_password": PASSWORD_TEMPLATE[3:21],
  "password1": PASSWORD_TEMPLATE[:10],
  "password2": PASSWORD_TEMPLATE[11:]
}

USER_DATA_OLD_AND_NEW_PASSWORDS_ARE_EQUAL = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "old_password": PASSWORD_TEMPLATE[3:21],
  "password1": PASSWORD_TEMPLATE[3:21],
  "password2": PASSWORD_TEMPLATE[3:21]
}

"""
User data for TestCaseLogin
"""

SUCCESSFUL_LOGIN_DATA = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "password": PASSWORD_TEMPLATE[:15]
}

USER_DATA_WITH_WRONG_USERNAME = {
  "username": generate_random_string(12),
  "password": PASSWORD_TEMPLATE[:15]
}

USER_DATA_WITH_WRONG_PASSWORD = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "password": PASSWORD_TEMPLATE[5:19]
}

USER_DATA_LOGIN_WITHOUT_USERNAME = {
  "username": "",
  "password": PASSWORD_TEMPLATE[:15]
}

USER_DATA_LOGIN_WITHOUT_PASSWORD = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "password": ""
}


class TestCaseUserCreate:

    link = "http://bzteltestapi.pythonanywhere.com/users"

    def test_successful_user_registration(self):
        response = requests.post(self.link, json=SUCCESSFUL_REGISTRATION_DATA)
        assert response.status_code == 201, response.json()

    def test_failed_user_already_exists(self):
        response = requests.post(self.link, json=SUCCESSFUL_REGISTRATION_DATA)
        assert response.status_code == 400, response.json()

    def test_failed_user_registration_without_username(self):
        response = requests.post(self.link, json=USER_DATA_WITHOUT_USERNAME)
        assert response.status_code == 400, response.json()

    def test_failed_user_registration_without_password(self):
        response = requests.post(self.link, json=USER_DATA_WITHOUT_PASSWORD)
        assert response.status_code == 400, response.json()

    def test_failed_user_registration_too_long_username(self):
        response = requests.post(self.link, json=USER_DATA_TOO_LONG_USERNAME)
        assert response.status_code == 400, response.json()

    def test_failed_user_registration_too_long_password(self):
        response = requests.post(self.link, json=USER_DATA_TOO_LONG_PASSWORD)
        assert response.status_code == 400, response.json()

    def test_failed_not_equal_passwords(self):
        response = requests.post(self.link, json=USER_DATA_NOT_EQUAL_PASSWORDS)
        assert response.status_code == 400, response.json()

    def test_failed_short_password(self):
        response = requests.post(self.link, json=USER_DATA_SHORT_PASSWORD)
        assert response.status_code == 400, response.json()

    def test_successful_min_length_password(self):
        response = requests.post(self.link, json=USER_DATA_MIN_LENGTH_PASSWORD)
        assert response.status_code == 201, response.json()

    def test_failed_short_username(self):
        response = requests.post(self.link, json=USER_DATA_SHORT_USERNAME)
        assert response.status_code == 400, response.json()

    def test_failed_username_started_with_whitespace(self):
        response = requests.post(self.link, json=USER_DATA_USERNAME_STARTED_WITH_WHITESPACE)
        assert response.status_code == 400, response.json()

    def test_failed_username_contains_spec_symbols(self):
        response = requests.post(self.link, json=USER_DATA_USERNAME_WITH_SPECIAL_SYMBOLS)
        assert response.status_code == 400, response.json()


class TestCaseLogin:
    link = "http://bzteltestapi.pythonanywhere.com/login"

    def test_successful_login(self):
        response = requests.post(self.link, json=SUCCESSFUL_LOGIN_DATA)
        assert response.status_code == 200, response.json()
        assert response.json().get("access_token")

    def test_failed_wrong_username(self):
        response = requests.post(self.link, json=USER_DATA_WITH_WRONG_USERNAME)
        assert response.status_code == 404, response.json()

    def test_failed_wrong_password(self):
        response = requests.post(self.link, json=USER_DATA_WITH_WRONG_PASSWORD)
        assert response.status_code == 400, response.json()

    def test_failed_user_data_without_username(self):
        response = requests.post(self.link, json=USER_DATA_LOGIN_WITHOUT_USERNAME)
        assert response.status_code == 400, response.json()

    def test_failed_user_data_without_password(self):
        response = requests.post(self.link, json=USER_DATA_LOGIN_WITHOUT_PASSWORD)
        assert response.status_code == 400, response.json()


class TestCaseUserPasswordReplace:

    link = "http://bzteltestapi.pythonanywhere.com/users"

    def test_successful_password_replace(self):
        response = requests.put(self.link, json=SUCCESSFUL_PASSWORD_REPLACE_DATA)
        assert response.status_code == 202, response.json()

    def test_failed_check_password_replace(self):
        response = requests.put(self.link, json=SUCCESSFUL_PASSWORD_REPLACE_DATA)
        assert response.status_code == 400, response.json()

    def test_failed_incorrect_old_password(self):
        response = requests.put(self.link, json=USER_DATA_INCORRECT_OLD_PASSWORD)
        assert response.status_code == 400, response.json()

    def test_failed_old_and_new_passwords_are_equal(self):
        response = requests.put(self.link, json=USER_DATA_OLD_AND_NEW_PASSWORDS_ARE_EQUAL)
        assert response.status_code == 400

    def test_failed_new_passwords_are_not_equal(self):
        response = requests.put(self.link, json=USER_DATA_NEW_PASSWORDS_ARE_NOT_EQUAL)
        assert response.status_code == 400

    def test_failed_new_passwords_are_not_equal_2(self):
        response = requests.put(self.link, json=USER_DATA_NEW_PASSWORDS_ARE_NOT_EQUAL_2)
        assert response.status_code == 400

    def test_successful_new_password(self):
        response = requests.put(self.link, json=SUCCESSFUL_PASSWORD_REPLACE_DATA_WITH_NEW_PASSWORD)
        assert response.status_code == 400


