import pytest
import random
import requests
import string


def generate_random_string(string_length):
    letters = string.printable
    random_string = ''.join(random.choice(letters) for i in range(string_length))
    return random_string


def generate_random_non_ascii_string(string_length):
    letters = "абвгдеёжзийклмнопрстуфхцчшщьъэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЭЮЯ"
    random_non_ascii_string = ''.join(random.choice(letters) for i in range(string_length))
    return random_non_ascii_string

SUCCESSFUL_CREATED_USERNAME_TEMPLATE = generate_random_string(12)

USERNAME_SPEC_SYMBOLS_TEMPLATE = string.printable[62:]

PASSWORD_TEMPLATE = generate_random_string(21)

PASSWORD_NON_ASCII_TEMPLATE = "тестовый_пароль"

"""
User data for TestCaseUserRegistration
"""
#
# invalid_json = "{'a': 'b'}"'

REGISTRATION_SUCCESSFUL_DATA = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_WITH_EMPTY_USERNAME_FIELD = {
    "username": "",
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_WITH_EMPTY_PASSWORD1_PASSWORD2_FIELDS = {
    "username": generate_random_string(12),
    "password1": "",
    "password2": ""
}

REGISTRATION_WITH_EMPTY_PASSWORD1_FIELD = {
    "username": generate_random_string(12),
    "password1": "",
    "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_WITH_EMPTY_PASSWORD2_FIELD = {
    "username": generate_random_string(12),
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": ""
}

REGISTRATION_NOT_EQUAL_PASSWORD1_AND_PASSWORD2 = {
  "username": generate_random_string(12),
  "password1": PASSWORD_TEMPLATE[:9],
  "password2": PASSWORD_TEMPLATE[10:20]
}

REGISTRATION_USERNAME_LENGTH_50 = {
  "username": generate_random_string(50),
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_USERNAME_LENGTH_51 = {
  "username": generate_random_string(51),
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_USERNAME_LENGTH_32 = {
  "username": generate_random_string(32),
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_USERNAME_LENGTH_33 = {
  "username": generate_random_string(33),
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_USERNAME_LENGTH_1 = {
  "username": generate_random_string(1),
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_USERNAME_LENGTH_6 = {
    "username": generate_random_string(6),
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_USERNAME_LENGTH_5 = {
    "username": generate_random_string(5),
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_20 = {
  "username": generate_random_string(12),
  "password1": PASSWORD_TEMPLATE[:20],
  "password2": PASSWORD_TEMPLATE[:20]
}

REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_21 = {
  "username": generate_random_string(12),
  "password1": PASSWORD_TEMPLATE[:21],
  "password2": PASSWORD_TEMPLATE[:21]
}

REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_1 = {
    "username": generate_random_string(12),
    "password1": PASSWORD_TEMPLATE[:1],
    "password2": PASSWORD_TEMPLATE[:1]
}

REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_6 = {
    "username": generate_random_string(12),
    "password1": PASSWORD_TEMPLATE[:6],
    "password2": PASSWORD_TEMPLATE[:6]
}

REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_5 = {
    "username": generate_random_string(12),
    "password1": PASSWORD_TEMPLATE[:5],
    "password2": PASSWORD_TEMPLATE[:5]
}

REGISTRATION_USERNAME_WITH_SPECIAL_SYMBOLS = {
    "username": USERNAME_SPEC_SYMBOLS_TEMPLATE,
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_USERNAME_STARTED_WITH_WHITESPACE = {
    "username": " " + generate_random_string(12),
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_WITH_EMPTY_FIELDS = {
    "username": "",
    "password1": "",
    "password2": ""
}

REGISTRATION_PASSWORD1_IS_PASSWORDS2_SUBSET = {
    "username": generate_random_string(12),
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": PASSWORD_TEMPLATE[:17]
}

REGISTRATION_PASSWORD2_IS_PASSWORDS1_SUBSET = {
    "username": generate_random_string(12),
    "password1": PASSWORD_TEMPLATE[:17],
    "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_NON_ASCII_SYMBOLS_IN_USERNAME = {
    "username": generate_random_non_ascii_string(12),
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": PASSWORD_TEMPLATE[:15]
}

REGISTRATION_NON_ASCII_SYMBOLS_IN_PASSWORD = {
    "username": generate_random_string(12),
    "password1": PASSWORD_NON_ASCII_TEMPLATE,
    "password2": PASSWORD_NON_ASCII_TEMPLATE
}

REGISTRATION_UPPERCASE_PASSWORD2 = {
    "username": generate_random_string(12),
    "password1": PASSWORD_TEMPLATE[:15],
    "password2": PASSWORD_TEMPLATE[:15].upper()
}


"""
User data for TestCaseLogin
"""

LOGIN_SUCCESSFUL_DATA = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "password": PASSWORD_TEMPLATE[:15]
}

LOGIN_WITH_WRONG_USERNAME = {
  "username": generate_random_string(12),
  "password": PASSWORD_TEMPLATE[:15]
}

LOGIN_WITH_WRONG_PASSWORD = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "password": PASSWORD_TEMPLATE[5:19]
}

LOGIN_WITHOUT_USERNAME = {
  "username": "",
  "password": PASSWORD_TEMPLATE[:15]
}

LOGIN_WITHOUT_PASSWORD = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "password": ""
}

"""
User data for TestCaseUserPasswordReplace
"""

REPLACE_PASSWORD_SUCCESSFUL = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "old_password": PASSWORD_TEMPLATE[:15],
  "password1": PASSWORD_TEMPLATE[3:21],
  "password2": PASSWORD_TEMPLATE[3:21]
}

REPLACE_PASSWORD_SUCCESSFUL_WITH_NEW_PASSWORD = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "old_password": PASSWORD_TEMPLATE[3:21],
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:15]
}

REPLACE_INCORRECT_OLD_PASSWORD = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "old_password": PASSWORD_TEMPLATE[:17],
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:15]
}

REPLACE_PASSWORD1_IS_SET = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "old_password": PASSWORD_TEMPLATE[3:21],
  "password1": PASSWORD_TEMPLATE[:15],
  "password2": PASSWORD_TEMPLATE[:17]
}

REPLACE_PASSWORDS_ARE_NOT_EQUAL = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "old_password": PASSWORD_TEMPLATE[3:21],
  "password1": PASSWORD_TEMPLATE[:10],
  "password2": PASSWORD_TEMPLATE[11:]
}

REPLACE_OLD_AND_NEW_PASSWORDS_ARE_EQUAL = {
  "username": SUCCESSFUL_CREATED_USERNAME_TEMPLATE,
  "old_password": PASSWORD_TEMPLATE[3:21],
  "password1": PASSWORD_TEMPLATE[3:21],
  "password2": PASSWORD_TEMPLATE[3:21]
}


class TestCaseUserRegistration:

    link = "http://bzteltestapi.pythonanywhere.com/users"

    def test_successful_user_registration(self):
        response = requests.post(self.link, json=REGISTRATION_SUCCESSFUL_DATA)
        assert response.status_code == 201, response.json()

    def test_failed_username_already_exists(self):
        response = requests.post(self.link, json=REGISTRATION_SUCCESSFUL_DATA)
        assert response.status_code == 400, response.json()

    def test_failed_registration_with_empty_username_field(self):
        response = requests.post(self.link, json=REGISTRATION_WITH_EMPTY_USERNAME_FIELD)
        assert response.status_code == 400, response.json()

    def test_failed_registration_with_empty_password1_password2_fields(self):
        response = requests.post(self.link, json=REGISTRATION_WITH_EMPTY_PASSWORD1_PASSWORD2_FIELDS)
        assert response.status_code == 400, response.json()

    def test_failed_registration_with_empty_password1_field(self):
        response = requests.post(self.link, json=REGISTRATION_WITH_EMPTY_PASSWORD1_FIELD)
        assert response.status_code == 400, response.json()

    def test_failed_registration_with_empty_password2_field(self):
        response = requests.post(self.link, json=REGISTRATION_WITH_EMPTY_PASSWORD2_FIELD)
        assert response.status_code == 400, response.json()

    def test_failed_registration_not_equal_password1_and_password2(self):
        response = requests.post(self.link, json=REGISTRATION_NOT_EQUAL_PASSWORD1_AND_PASSWORD2)
        assert response.status_code == 400, response.json()

    def test_successful_registration_username_length_50(self):
        response = requests.post(self.link, json=REGISTRATION_USERNAME_LENGTH_50)
        assert response.status_code == 201, response.json()

    def test_failed_registration_username_length_51(self):
        response = requests.post(self.link, json=REGISTRATION_USERNAME_LENGTH_51)
        assert response.status_code == 400, response.json()

    def test_successful_registration_username_length_32(self):
        response = requests.post(self.link, json=REGISTRATION_USERNAME_LENGTH_32)
        assert response.status_code == 201, response.json()

    def test_failed_registration_username_length_33(self):
        response = requests.post(self.link, json=REGISTRATION_USERNAME_LENGTH_33)
        assert response.status_code == 400, response.json()

    def test_successful_registration_username_length_1(self):
        response = requests.post(self.link, json=REGISTRATION_USERNAME_LENGTH_1)
        assert response.status_code == 201, response.json()

    def test_successful_registration_username_length_6(self):
        response = requests.post(self.link, json=REGISTRATION_USERNAME_LENGTH_6)
        assert response.status_code == 201, response.json()

    def test_failed_registration_username_length_5(self):
        response = requests.post(self.link, json=REGISTRATION_USERNAME_LENGTH_5)
        assert response.status_code == 400, response.json()

    def test_successful_registration_password1_password2_length_20(self):
        response = requests.post(self.link, json=REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_20)
        assert response.status_code == 201, response.json()

    def test_failed_registration_password1_password2_length_21(self):
        response = requests.post(self.link, json=REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_21)
        assert response.status_code == 400, response.json()

    def test_successful_registration_password1_password2_length_1(self):
        response = requests.post(self.link, json=REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_1)
        assert response.status_code == 201, response.json()

    def test_successful_registration_password1_password2_length_6(self):
        response = requests.post(self.link, json=REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_6)
        assert response.status_code == 201, response.json()

    def test_failed_registration_password1_password2_length_5(self):
        response = requests.post(self.link, json=REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_5)
        assert response.status_code == 400, response.json()

    def test_failed_registration_username_started_with_whitespace(self):
        response = requests.post(self.link, json=REGISTRATION_USERNAME_STARTED_WITH_WHITESPACE)
        assert response.status_code == 400, response.json()

    def test_failed_registration_username_contains_spec_symbols(self):
        response = requests.post(self.link, json=REGISTRATION_USERNAME_WITH_SPECIAL_SYMBOLS)
        assert response.status_code == 400, response.json()

    def test_failed_registration_with_empty_fields(self):
        response = requests.post(self.link, json=REGISTRATION_WITH_EMPTY_FIELDS)
        assert response.status_code == 400, response.json()

    def test_failed_registration_password1_is_passwords2_subset(self):
        response = requests.post(self.link, json=REGISTRATION_PASSWORD1_IS_PASSWORDS2_SUBSET)
        assert response.status_code == 400, response.json()

    def test_failed_registration_password2_is_passwords1_subset(self):
        response = requests.post(self.link, json=REGISTRATION_PASSWORD2_IS_PASSWORDS1_SUBSET)
        assert response.status_code == 400, response.json()

    def test_failed_registration_non_ascii_symbols_in_username(self):
        response = requests.post(self.link, json=REGISTRATION_NON_ASCII_SYMBOLS_IN_USERNAME)
        assert response.status_code == 400, response.json()

    def test_successful_registration_non_ascii_symbols_in_password(self):
        response = requests.post(self.link, json=REGISTRATION_NON_ASCII_SYMBOLS_IN_PASSWORD)
        assert response.status_code == 201, response.json()

    def test_failed_registration_non_ascii_symbols_in_password(self):
        response = requests.post(self.link, json=REGISTRATION_UPPERCASE_PASSWORD2)
        assert response.status_code == 400, response.json()




@pytest.mark.skip
class TestCaseUserLogin:
    link = "http://bzteltestapi.pythonanywhere.com/login"

    def test_successful_login(self):
        response = requests.post(self.link, json=LOGIN_SUCCESSFUL_DATA)
        assert response.status_code == 200, response.json()
        assert response.json().get("access_token")

    def test_failed_login_wrong_username(self):
        response = requests.post(self.link, json=LOGIN_WITH_WRONG_USERNAME)
        assert response.status_code == 404, response.json()

    def test_failed_login_with_wrong_password(self):
        response = requests.post(self.link, json=LOGIN_WITH_WRONG_PASSWORD)
        assert response.status_code == 400, response.json()

    def test_failed_login_without_username(self):
        response = requests.post(self.link, json=LOGIN_WITHOUT_USERNAME)
        assert response.status_code == 400, response.json()

    def test_failed_login_without_password(self):
        response = requests.post(self.link, json=LOGIN_WITHOUT_PASSWORD)
        assert response.status_code == 400, response.json()


@pytest.mark.skip
class TestCaseUserPasswordReplace:

    link = "http://bzteltestapi.pythonanywhere.com/users"

    def test_successful_password_replace(self):
        response = requests.put(self.link, json=REPLACE_PASSWORD_SUCCESSFUL)
        assert response.status_code == 202, response.json()

    def test_failed_replace_check_password(self):
        response = requests.put(self.link, json=REPLACE_PASSWORD_SUCCESSFUL)
        assert response.status_code == 400, response.json()

    def test_failed_replace_incorrect_old_password(self):
        response = requests.put(self.link, json=REPLACE_INCORRECT_OLD_PASSWORD)
        assert response.status_code == 400, response.json()

    def test_failed_replace_old_and_new_passwords_are_equal(self):
        response = requests.put(self.link, json=REPLACE_OLD_AND_NEW_PASSWORDS_ARE_EQUAL)
        assert response.status_code == 400

    def test_failed_replace_new_passwords_are_not_equal(self):
        response = requests.put(self.link, json=REPLACE_PASSWORD1_IS_SET)
        assert response.status_code == 400

    def test_failed_replace_new_passwords_are_not_equal_2(self):
        response = requests.put(self.link, json=REPLACE_PASSWORDS_ARE_NOT_EQUAL)
        assert response.status_code == 400

    def test_successful_replace_new_password(self):
        response = requests.put(self.link, json=REPLACE_PASSWORD_SUCCESSFUL_WITH_NEW_PASSWORD)
        assert response.status_code == 400


