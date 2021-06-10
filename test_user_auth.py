import pytest
import jwt
import requests
import user_data


class TestCaseUserRegistration:

    link = "http://bzteltestapi.pythonanywhere.com/users"

    test_cases = [
        pytest.param("POST", user_data.REGISTRATION_SUCCESSFUL_DATA, 201, id="test_successful_user_registration"),
        pytest.param("POST", user_data.REGISTRATION_SUCCESSFUL_DATA, 400, id="test_failed_username_already_exists"),
        pytest.param("POST", user_data.REGISTRATION_WITH_EMPTY_USERNAME_FIELD, 400, id="test_failed_registration_with_empty_username_field"),
        pytest.param("POST", user_data.REGISTRATION_WITH_EMPTY_PASSWORD1_PASSWORD2_FIELDS, 400, id="test_failed_registration_with_empty_password1_password2_fields"),
        pytest.param("POST", user_data.REGISTRATION_WITH_EMPTY_PASSWORD1_FIELD, 400, id="test_failed_registration_with_empty_password1_field"),
        pytest.param("POST", user_data.REGISTRATION_WITH_EMPTY_PASSWORD2_FIELD, 400, id="test_failed_registration_with_empty_password2_field"),
        pytest.param("POST", user_data.REGISTRATION_NOT_EQUAL_PASSWORD1_AND_PASSWORD2, 400, id="test_failed_registration_not_equal_password1_and_password2"),
        pytest.param("POST", user_data.REGISTRATION_USERNAME_LENGTH_50, 201, id="test_successful_registration_username_length_50"),
        pytest.param("POST", user_data.REGISTRATION_USERNAME_LENGTH_51, 400, id="test_failed_registration_username_length_51"),
        pytest.param("POST", user_data.REGISTRATION_USERNAME_LENGTH_32, 201, id="test_successful_registration_username_length_32"),
        pytest.param("POST", user_data.REGISTRATION_USERNAME_LENGTH_33, 400, id="test_failed_registration_username_length_33"),
        pytest.param("POST", user_data.REGISTRATION_USERNAME_LENGTH_1, 201, id="test_successful_registration_username_length_1"),
        pytest.param("POST", user_data.REGISTRATION_USERNAME_LENGTH_6, 201, id="test_successful_registration_username_length_6"),
        pytest.param("POST", user_data.REGISTRATION_USERNAME_LENGTH_5, 400, id="test_failed_registration_username_length_5"),
        pytest.param("POST", user_data.REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_20, 201, id="test_successful_registration_password1_password2_length_20"),
        pytest.param("POST", user_data.REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_21, 400, id="test_failed_registration_password1_password2_length_21"),
        pytest.param("POST", user_data.REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_1, 201, id="test_successful_registration_password1_password2_length_1"),
        pytest.param("POST", user_data.REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_6, 201, id="test_successful_registration_password1_password2_length_6"),
        pytest.param("POST", user_data.REGISTRATION_PASSWORD1_PASSWORD2_LENGTH_5, 400, id="test_failed_registration_password1_password2_length_5"),
        pytest.param("POST", user_data.REGISTRATION_USERNAME_STARTED_WITH_WHITESPACE, 400, id="test_failed_registration_username_started_with_whitespace"),
        pytest.param("POST", user_data.REGISTRATION_USERNAME_WITH_SPECIAL_SYMBOLS, 400, id="test_failed_registration_username_contains_spec_symbols"),
        pytest.param("POST", user_data.REGISTRATION_WITH_EMPTY_FIELDS, 400, id="test_failed_registration_with_empty_fields"),
        pytest.param("POST", user_data.REGISTRATION_PASSWORD1_IS_PASSWORDS2_SUBSET, 400, id="test_failed_registration_password1_is_passwords2_subset"),
        pytest.param("POST", user_data.REGISTRATION_PASSWORD2_IS_PASSWORDS1_SUBSET, 400, id="test_failed_registration_password2_is_passwords1_subset"),
        pytest.param("POST", user_data.REGISTRATION_NON_ASCII_SYMBOLS_IN_USERNAME, 400, id="test_failed_registration_non_ascii_symbols_in_username"),
        pytest.param("POST", user_data.REGISTRATION_NON_ASCII_SYMBOLS_IN_PASSWORD, 201, id="test_successful_registration_non_ascii_symbols_in_password"),
        pytest.param("POST", user_data.REGISTRATION_UPPERCASE_PASSWORD2, 400, id="test_failed_registration_different_passwords_cases"),
    ]

    @pytest.mark.parametrize("method,payload,expected_status_code", test_cases)
    def test_request(self, method, payload, expected_status_code):
        response = requests.request(method, self.link, json=payload)
        assert response.status_code == expected_status_code, response.json()


class TestCaseUserLogin:

    link = "http://bzteltestapi.pythonanywhere.com/login"

    test_cases = [
        pytest.param("POST", user_data.LOGIN_WITH_WRONG_USERNAME, 404, id="test_failed_login_wrong_username"),
        pytest.param("POST", user_data.LOGIN_WITH_WRONG_PASSWORD, 400, id="test_failed_login_with_wrong_password"),
        pytest.param("POST", user_data.LOGIN_WITHOUT_USERNAME, 400, id="test_failed_login_without_username"),
        pytest.param("POST", user_data.LOGIN_WITHOUT_PASSWORD, 400, id="test_failed_login_without_password"),
        pytest.param("POST", user_data.LOGIN_WITH_EMPTY_FIELDS, 400, id="test_failed_login_with_empty_fields"),
    ]

    def test_successful_login(self):
        response = requests.post(self.link, json=user_data.LOGIN_SUCCESSFUL_DATA)
        assert response.status_code == 200, response.json()
        token = response.json().get("access_token")
        try:
            jwt.decode(token, options={"verify_signature": False}, algorithms=['HS256', 'RS256'])
        except jwt.PyJWTError:
            raise AssertionError('Invalid JWT-token received')

    @pytest.mark.parametrize("method,payload,expected_status_code", test_cases)
    def test_request(self, method, payload, expected_status_code):
        response = requests.request(method, self.link, json=payload)
        assert response.status_code == expected_status_code, response.json()


class TestCaseUserPasswordReplace:

    link = "http://bzteltestapi.pythonanywhere.com/users"

    test_cases = [
        pytest.param("PUT", user_data.REPLACE_PASSWORD_SUCCESSFUL, 202, id="test_successful_password_replace"),
        pytest.param("PUT", user_data.REPLACE_PASSWORD_SUCCESSFUL, 400, id="test_failed_try_to_replace_with_old_password"),
        pytest.param("PUT", user_data.REPLACE_INCORRECT_OLD_PASSWORD, 400, id="test_failed_replace_incorrect_old_password"),
        pytest.param("PUT", user_data.REPLACE_OLD_AND_NEW_PASSWORDS_ARE_EQUAL, 400, id="test_failed_replace_old_and_new_passwords_are_equal"),
        pytest.param("PUT", user_data.REPLACE_PASSWORD1_IS_PASSWORDS2_SUBSET, 400, id="test_failed_replace_password1_is_passwords2_subset"),
        pytest.param("PUT", user_data.REPLACE_PASSWORD2_IS_PASSWORDS1_SUBSET, 400, id="test_failed_replace_password2_is_passwords1_subset"),
        pytest.param("PUT", user_data.REPLACE_PASSWORDS_ARE_NOT_EQUAL, 400, id="test_failed_replace_new_passwords_are_not_equal"),
        pytest.param("PUT", user_data.REPLACE_WITH_EMPTY_USERNAME_FIELD, 400, id="test_failed_replace_with_empty_username_field"),
        pytest.param("PUT", user_data.REPLACE_WITH_EMPTY_OLD_PASSWORD_FIELD, 400, id="test_failed_replace_with_empty_old_password_field"),
        pytest.param("PUT", user_data.REPLACE_WITH_EMPTY_PASSWORD1_FIELD, 400, id="test_failed_replace_with_empty_password1_field"),
        pytest.param("PUT", user_data.REPLACE_WITH_EMPTY_PASSWORD2_FIELD, 400, id="test_failed_replace_with_empty_password2_field"),
    ]

    @pytest.mark.parametrize("method,payload,expected_status_code", test_cases)
    def test_request(self, method, payload, expected_status_code):
        response = requests.request(method, self.link, json=payload)
        assert response.status_code == expected_status_code, response.json()


