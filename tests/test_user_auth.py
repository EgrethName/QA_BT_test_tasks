import copy

import jwt
import pytest
import requests

from user_data import LoginData, MixedTestsData, PasswordReplaceData, RegistrationData

GET = "GET"
POST = "POST"
PUT = "PUT"
DELETE = "DELETE"
PATCH = "PATCH"
HEAD = "HEAD"
OPTIONS = "OPTIONS"

HOME_LINK = "http://bzteltestapi.pythonanywhere.com"
USERS_LINK = "http://bzteltestapi.pythonanywhere.com/users"
LOGIN_LINK = "http://bzteltestapi.pythonanywhere.com/login"


# @pytest.mark.skip
class TestCaseUserRegistration:

    method = "POST"

    test_cases = [
        pytest.param(POST, RegistrationData.REGISTRATION_SUCCESSFUL, 201, id="test_successful_user_registration"),
        pytest.param(POST, RegistrationData.REGISTRATION_SUCCESSFUL_WITH_CORRECT_DATA, 201, id="test_successful_user_registration_with_correct_data"),
        pytest.param(POST, RegistrationData.REGISTRATION_SUCCESSFUL_WITH_CORRECT_DATA, 400, id="test_failed_username_already_exists"),
        pytest.param(POST, RegistrationData.REGISTRATION_WITH_EMPTY_USERNAME_FIELD, 400, id="test_failed_registration_with_empty_username_field"),
        pytest.param(POST, RegistrationData.REGISTRATION_WITH_EMPTY_PASSWORD1_PASSWORD2_FIELDS, 400, id="test_failed_registration_with_empty_password1_password2_fields"),
        pytest.param(POST, RegistrationData.REGISTRATION_WITH_EMPTY_PASSWORD1_FIELD, 400, id="test_failed_registration_with_empty_password1_field"),
        pytest.param(POST, RegistrationData.REGISTRATION_WITH_EMPTY_PASSWORD2_FIELD, 400, id="test_failed_registration_with_empty_password2_field"),
        pytest.param(POST, RegistrationData.REGISTRATION_NOT_EQUAL_PASSWORD1_AND_PASSWORD2, 400, id="test_failed_registration_not_equal_password1_and_password2"),
        pytest.param(POST, RegistrationData.REGISTRATION_USERNAME_LENGTH_50, 201, id="test_successful_registration_username_length_50"),
        pytest.param(POST, RegistrationData.REGISTRATION_USERNAME_LENGTH_51, 400, id="test_failed_registration_username_length_51"),
        pytest.param(POST, RegistrationData.REGISTRATION_USERNAME_LENGTH_32, 201, id="test_successful_registration_username_length_32"),
        pytest.param(POST, RegistrationData.REGISTRATION_USERNAME_LENGTH_33, 400, id="test_failed_registration_username_length_33"),
        pytest.param(POST, RegistrationData.REGISTRATION_USERNAME_LENGTH_1, 201, id="test_successful_registration_username_length_1"),
        pytest.param(POST, RegistrationData.REGISTRATION_USERNAME_LENGTH_6, 201, id="test_successful_registration_username_length_6"),
        pytest.param(POST, RegistrationData.REGISTRATION_USERNAME_LENGTH_5, 400, id="test_failed_registration_username_length_5"),
        pytest.param(POST, RegistrationData.REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_20, 201, id="test_successful_registration_password1_password2_length_20"),
        pytest.param(POST, RegistrationData.REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_21, 400, id="test_failed_registration_password1_password2_length_21"),
        pytest.param(POST, RegistrationData.REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_1, 201, id="test_successful_registration_password1_password2_length_1"),
        pytest.param(POST, RegistrationData.REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_6, 201, id="test_successful_registration_password1_password2_length_6"),
        pytest.param(POST, RegistrationData.REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_5, 400, id="test_failed_registration_password1_password2_length_5"),
        pytest.param(POST, RegistrationData.REGISTRATION_USERNAME_WITH_WHITESPACE, 400, id="test_failed_registration_username_with_whitespace"),
        pytest.param(POST, RegistrationData.REGISTRATION_PASSWORD_WITH_WHITESPACE, 400, id="test_failed_registration_password_with_whitespace"),
        pytest.param(POST, RegistrationData.REGISTRATION_USERNAME_WITH_SPECIAL_SYMBOLS, 400, id="test_failed_registration_username_contains_spec_symbols"),
        pytest.param(POST, RegistrationData.REGISTRATION_WITH_EMPTY_FIELDS, 400, id="test_failed_registration_with_empty_fields"),
        pytest.param(POST, RegistrationData.REGISTRATION_NON_ASCII_SYMBOLS_IN_USERNAME, 400, id="test_failed_registration_non_ascii_symbols_in_username"),
        pytest.param(POST, RegistrationData.REGISTRATION_NON_ASCII_SYMBOLS_IN_PASSWORD, 201, id="test_successful_registration_non_ascii_symbols_in_password"),
        pytest.param(POST, RegistrationData.REGISTRATION_UPPERCASE_PASSWORD2, 400, id="test_failed_registration_different_passwords_cases"),
        pytest.param(POST, RegistrationData.REGISTRATION_WITH_EXCESS_DATA, 201, id="test_successful_registration_with_excess_data"),
    ]

    @pytest.mark.parametrize("method,payload,expected_status_code", test_cases)
    def test_request(self, method, payload, expected_status_code):
        response = requests.request(method, USERS_LINK, json=payload)
        assert response.json()
        assert response.status_code == expected_status_code, response.json()


# @pytest.mark.skip
class TestCaseUserLogin:

    test_cases = [
        pytest.param(POST, LoginData.LOGIN_WITH_WRONG_USERNAME, 404, id="test_failed_login_wrong_username"),
        pytest.param(POST, LoginData.LOGIN_WITH_WRONG_PASSWORD, 400, id="test_failed_login_with_wrong_password"),
        pytest.param(POST, LoginData.LOGIN_WITHOUT_USERNAME, 400, id="test_failed_login_without_username"),
        pytest.param(POST, LoginData.LOGIN_WITHOUT_PASSWORD, 400, id="test_failed_login_without_password"),
        pytest.param(POST, LoginData.LOGIN_WITH_EMPTY_FIELDS, 400, id="test_failed_login_with_empty_fields"),
    ]

    def setup_class(self):
        response = requests.request(POST, USERS_LINK, json=LoginData.REGISTRATION_SUCCESSFUL)
        assert response.status_code == 201, response.json()

    def test_successful_login(self):
        response = requests.post(LOGIN_LINK, json=LoginData.LOGIN_SUCCESSFUL_DATA)
        assert response.status_code == 200, response.json()
        assert response.json()
        token = response.json().get("access_token")
        try:
            jwt.decode(token, options={"verify_signature": False}, algorithms=['HS256', 'RS256'])
        except jwt.PyJWTError:
            raise AssertionError('Invalid JWT-token received')

    @pytest.mark.parametrize("method,payload,expected_status_code", test_cases)
    def test_request(self, method, payload, expected_status_code):
        response = requests.request(method, LOGIN_LINK, json=payload)
        assert response.status_code == expected_status_code, response.json()
        assert response.json()


# @pytest.mark.skip
class TestCaseUserPasswordReplace:

    test_cases = [
        pytest.param(PUT, PasswordReplaceData.REPLACE_PASSWORD_SUCCESSFUL, 202, id="test_successful_password_replace"),
        pytest.param(PUT, PasswordReplaceData.REPLACE_PASSWORD_SUCCESSFUL, 400, id="test_failed_try_to_replace_with_old_password"),
        pytest.param(PUT, PasswordReplaceData.REPLACE_INCORRECT_OLD_PASSWORD, 400, id="test_failed_replace_incorrect_old_password"),
        pytest.param(PUT, PasswordReplaceData.REPLACE_OLD_AND_NEW_PASSWORDS_ARE_EQUAL, 400, id="test_failed_replace_old_and_new_passwords_are_equal"),
        pytest.param(PUT, PasswordReplaceData.REPLACE_PASSWORDS_ARE_NOT_EQUAL, 400, id="test_failed_replace_new_passwords_are_not_equal"),
        pytest.param(PUT, PasswordReplaceData.REPLACE_PASSWORD1_PASSWORD2_MORE_THAN_20, 400, id="test_failed_replace_password1_password2_more_than_20"),
        pytest.param(PUT, PasswordReplaceData.REPLACE_PASSWORD1_PASSWORD2_LESS_THAN_6, 400, id="test_failed_replace_password1_password2_less_than_6"),
        pytest.param(PUT, PasswordReplaceData.REPLACE_WITH_EMPTY_USERNAME_FIELD, 400, id="test_failed_replace_with_empty_username_field"),
        pytest.param(PUT, PasswordReplaceData.REPLACE_WITH_EMPTY_OLD_PASSWORD_FIELD, 400, id="test_failed_replace_with_empty_old_password_field"),
        pytest.param(PUT, PasswordReplaceData.REPLACE_WITH_EMPTY_PASSWORD1_FIELD, 400, id="test_failed_replace_with_empty_password1_field"),
        pytest.param(PUT, PasswordReplaceData.REPLACE_WITH_EMPTY_PASSWORD2_FIELD, 400, id="test_failed_replace_with_empty_password2_field"),
        pytest.param(PUT, PasswordReplaceData.REPLACE_WITH_EMPTY_PASSWORD2_FIELD, 400, id="test_failed_replace_with_empty_fields"),
    ]

    def setup_class(self):
        response = requests.request(POST, USERS_LINK, json=PasswordReplaceData.REGISTRATION_SUCCESSFUL)
        assert response.status_code == 201, response.json()

    @pytest.mark.parametrize("method,payload,expected_status_code", test_cases)
    def test_request(self, method, payload, expected_status_code):
        response = requests.request(method, USERS_LINK, json=payload)
        try:
            assert response.status_code == expected_status_code, response.json()
        except AssertionError:
            result_msg = response.json().get('result')
            if result_msg == 'Password successfully updated!':
                new_payload = copy.deepcopy(payload)
                new_payload['password1'] = payload['old_password']
                new_payload['password2'] = payload['old_password']
                new_payload['old_password'] = payload['password1']
                requests.request(method, USERS_LINK, json=new_payload)
            raise AssertionError

        assert response.json()



# @pytest.mark.skip
class TestCaseCheckHTTPMethods:

    home_methods = [pytest.param(GET, 200, id="test_GET_method"),
                    pytest.param(PUT, 405, id="test_PUT_method"),
                    pytest.param(POST, 405, id="test_POST_method"),
                    pytest.param(PATCH, 405, id="test_PATCH_method"),
                    pytest.param(DELETE, 405, id="test_DELETE_method"),
                    pytest.param(HEAD, 200, id="test_HEAD_method"),
                    pytest.param(OPTIONS, 200, id="test_OPTIONS_method")]

    @pytest.mark.parametrize("method,expected_status_code", home_methods)
    def test_http_home_methods(self, method, expected_status_code):
        response = requests.request(method, HOME_LINK)
        assert response.status_code == expected_status_code

    users_methods = [pytest.param(GET, 405, id="test_GET_method"),
                     pytest.param(PATCH, 405, id="test_PATCH_method"),
                     pytest.param(DELETE, 405, id="test_DELETE_method"),
                     pytest.param(HEAD, 405, id="test_HEAD_method"),
                     pytest.param(OPTIONS, 200, id="test_OPTIONS_method")]

    @pytest.mark.parametrize("method,expected_status_code", users_methods)
    def test_http_users_methods(self, method, expected_status_code):
        response = requests.request(method, USERS_LINK)
        assert response.status_code == expected_status_code

    login_methods = [pytest.param(GET, 405, id="test_GET_method"),
                     pytest.param(PUT, 405, id="test_PUT_method"),
                     pytest.param(PATCH, 405, id="test_PATCH_method"),
                     pytest.param(DELETE, 405, id="test_DELETE_method"),
                     pytest.param(HEAD, 405, id="test_HEAD_method"),
                     pytest.param(OPTIONS, 200, id="test_OPTIONS_method")]

    @pytest.mark.parametrize("method,expected_status_code", login_methods)
    def test_http_login_methods(self, method, expected_status_code):
        response = requests.request(method, LOGIN_LINK)
        assert response.status_code == expected_status_code


# @pytest.mark.skip
class TestCaseMixedTests:

    todo_link = "http://bzteltestapi.pythonanywhere.com/todos/" + MixedTestsData.REG_USERNAME

    def setup_class(self):
        response = requests.request(POST, USERS_LINK, json=MixedTestsData.REGISTRATION_SUCCESSFUL)
        assert response.status_code == 201, response.json()

    def test_failed_login_with_old_password(self):
        requests.request(PUT, USERS_LINK, json=MixedTestsData.MIXED_REPLACE_PASSWORD_SUCCESSFUL)
        response = requests.request(POST, LOGIN_LINK, json=MixedTestsData.MIXED_LOGIN_WITH_OLD_PASSWORD)
        assert response.status_code == 400, response.json()
        assert response.json()

    def test_successful_login_with_new_password(self):
        response = requests.request(POST, LOGIN_LINK, json=MixedTestsData.MIXED_LOGIN_WITH_NEW_PASSWORD)
        assert response.status_code == 200, response.json()
        assert response.json()

    def test_successful_create_todo_with_jwt_token(self):
        login_response = requests.request(POST, LOGIN_LINK, json=MixedTestsData.MIXED_LOGIN_WITH_NEW_PASSWORD)
        jwt_token = login_response.json().get("access_token")
        jwt_header = {"Authorization": "Bearer" + " " + jwt_token}
        todo_response = requests.request(POST, self.todo_link, headers=jwt_header,
                                         json=MixedTestsData.MIXED_TODO_SUCCESSFUL_CREATE)
        assert todo_response.status_code == 201, todo_response.json()
        assert todo_response.json()

    def test_failed_expired_jwt_token(self):
        first_login_response = requests.request(POST, LOGIN_LINK, json=MixedTestsData.MIXED_LOGIN_WITH_NEW_PASSWORD)
        first_jwt_token = first_login_response.json().get("access_token")
        first_jwt_header = {"Authorization": "Bearer" + " " + first_jwt_token}
        requests.request(PUT, USERS_LINK, json=MixedTestsData.MIXED_SECOND_REPLACE_PASSWORD_SUCCESSFUL)
        todo_response = requests.request(POST, self.todo_link, headers=first_jwt_header,
                                         json=MixedTestsData.MIXED_TODO_SUCCESSFUL_CREATE)
        assert todo_response.status_code == 401, todo_response.json()
        assert todo_response.json()
