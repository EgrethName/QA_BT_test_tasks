import random


def generate_random_string(string_length):
    letters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"
    random_string = ''.join(random.choice(letters) for i in range(string_length))
    return random_string


def generate_random_non_ascii_string(string_length):
    letters = "абвгдеёжзийклмнопрстуфхцчшщьъэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЭЮЯ"
    random_non_ascii_string = ''.join(random.choice(letters) for i in range(string_length))
    return random_non_ascii_string


USERNAME_SPEC_SYMBOLS_TEMPLATE = '/&?#$+,:;=@\'/'
PASSWORD_TEMPLATE = generate_random_string(21)
PASSWORD_NON_ASCII_TEMPLATE = "тестовый_пароль"
PASSWORD_WITH_WHITESPACE = " " + generate_random_string(6) + " " + generate_random_string(6) + " "

"""
User data for TestCaseUserRegistration
"""


class RegistrationData:

    REG_USERNAME = generate_random_string(12)

    REGISTRATION_SUCCESSFUL = {
      "username": generate_random_string(12),
      "password1": PASSWORD_TEMPLATE[:15],
      "pasword2": PASSWORD_TEMPLATE[:15]
    }

    REGISTRATION_SUCCESSFUL_WITH_CORRECT_DATA = {
      "username": generate_random_string(12),
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

    REGISTRATION_USERNAME_WITH_WHITESPACE = {
        "username": " " + generate_random_string(6) + " " + generate_random_string(6) + " ",
        "password1": PASSWORD_TEMPLATE[:15],
        "password2": PASSWORD_TEMPLATE[:15]
    }

    REGISTRATION_PASSWORD_WITH_WHITESPACE = {
        "username": generate_random_string(12),
        "password1": PASSWORD_WITH_WHITESPACE,
        "password2": PASSWORD_WITH_WHITESPACE
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

    REGISTRATION_WITH_EXCESS_DATA = {
      "username": generate_random_string(12),
      "username1": generate_random_string(12),
      "old_password": PASSWORD_TEMPLATE[10:17],
      "password1": PASSWORD_TEMPLATE[:15],
      "password2": PASSWORD_TEMPLATE[:15]
    }


"""
User data for TestCaseLogin
"""


class LoginData:
    REG_USERNAME = generate_random_string(12)

    REGISTRATION_SUCCESSFUL = {
      "username": REG_USERNAME,
      "password1": PASSWORD_TEMPLATE[:15],
      "password2": PASSWORD_TEMPLATE[:15]
    }

    LOGIN_SUCCESSFUL_DATA = {
      "username": REG_USERNAME,
      "password": PASSWORD_TEMPLATE[:15]
    }

    LOGIN_WITH_WRONG_USERNAME = {
      "username": generate_random_string(12),
      "password": PASSWORD_TEMPLATE[:15]
    }

    LOGIN_WITH_WRONG_PASSWORD = {
      "username": REG_USERNAME,
      "password": PASSWORD_TEMPLATE[5:19]
    }

    LOGIN_WITHOUT_USERNAME = {
      "username": "",
      "password": PASSWORD_TEMPLATE[:15]
    }

    LOGIN_WITHOUT_PASSWORD = {
      "username": REG_USERNAME,
      "password": ""
    }

    LOGIN_WITH_EMPTY_FIELDS = {
      "username": "",
      "password": ""
    }


"""
User data for TestCaseUserPasswordReplace
"""


class PasswordReplaceData:

    REG_USERNAME = generate_random_string(12)

    REGISTRATION_SUCCESSFUL = {
      "username": REG_USERNAME,
      "password1": PASSWORD_TEMPLATE[:15],
      "password2": PASSWORD_TEMPLATE[:15]
    }

    REPLACE_PASSWORD_SUCCESSFUL = {
      "username": REG_USERNAME,
      "old_password": PASSWORD_TEMPLATE[:15],
      "password1": PASSWORD_TEMPLATE[3:21],
      "password2": PASSWORD_TEMPLATE[3:21]
    }

    REPLACE_INCORRECT_OLD_PASSWORD = {
      "username": REG_USERNAME,
      "old_password": PASSWORD_TEMPLATE[:17],
      "password1": PASSWORD_TEMPLATE[:15],
      "password2": PASSWORD_TEMPLATE[:15]
    }

    REPLACE_OLD_AND_NEW_PASSWORDS_ARE_EQUAL = {
      "username": REG_USERNAME,
      "old_password": PASSWORD_TEMPLATE[3:21],
      "password1": PASSWORD_TEMPLATE[3:21],
      "password2": PASSWORD_TEMPLATE[3:21]
    }

    REPLACE_PASSWORDS_ARE_NOT_EQUAL = {
      "username": REG_USERNAME,
      "old_password": PASSWORD_TEMPLATE[3:21],
      "password1": PASSWORD_TEMPLATE[:10],
      "password2": PASSWORD_TEMPLATE[11:]
    }

    REPLACE_PASSWORD1_IS_PASSWORDS2_SUBSET = {
      "username": REG_USERNAME,
      "old_password": PASSWORD_TEMPLATE[3:21],
      "password1": PASSWORD_TEMPLATE[:15],
      "password2": PASSWORD_TEMPLATE[:17]
    }

    REPLACE_PASSWORD2_IS_PASSWORDS1_SUBSET = {
      "username": REG_USERNAME,
      "old_password": PASSWORD_TEMPLATE[3:21],
      "password1": PASSWORD_TEMPLATE[:17],
      "password2": PASSWORD_TEMPLATE[:15]
    }

    REPLACE_PASSWORD1_PASSWORD2_MORE_THAN_20 = {
      "username": REG_USERNAME,
      "old_password": PASSWORD_TEMPLATE[3:21],
      "password1": PASSWORD_TEMPLATE[:21],
      "password2": PASSWORD_TEMPLATE[:21]
    }

    REPLACE_PASSWORD1_PASSWORD2_LESS_THAN_6 = {
      "username": REG_USERNAME,
      "old_password": PASSWORD_TEMPLATE[3:21],
      "password1": PASSWORD_TEMPLATE[:5],
      "password2": PASSWORD_TEMPLATE[:5]
    }

    REPLACE_WITH_EMPTY_USERNAME_FIELD = {
      "username": "",
      "old_password": PASSWORD_TEMPLATE[:15],
      "password1": PASSWORD_TEMPLATE[3:21],
      "password2": PASSWORD_TEMPLATE[3:21]
    }

    REPLACE_WITH_EMPTY_OLD_PASSWORD_FIELD = {
      "username": REG_USERNAME,
      "old_password": "",
      "password1": PASSWORD_TEMPLATE[3:21],
      "password2": PASSWORD_TEMPLATE[3:21]
    }

    REPLACE_WITH_EMPTY_PASSWORD1_FIELD = {
      "username": REG_USERNAME,
      "old_password": PASSWORD_TEMPLATE[:15],
      "password1": "",
      "password2": PASSWORD_TEMPLATE[3:21]
    }

    REPLACE_WITH_EMPTY_PASSWORD2_FIELD = {
      "username": REG_USERNAME,
      "old_password": PASSWORD_TEMPLATE[:15],
      "password1": PASSWORD_TEMPLATE[3:21],
      "password2": ""
    }

    REPLACE_WITH_EMPTY_FIELDS = {
      "username": "",
      "old_password": "",
      "password1": "",
      "password2": ""
    }


"""
User data for TestCaseMixedTests
"""


class MixedTestsData:

    REG_USERNAME = generate_random_string(12)

    REGISTRATION_SUCCESSFUL = {
      "username": REG_USERNAME,
      "password1": PASSWORD_TEMPLATE[:15],
      "password2": PASSWORD_TEMPLATE[:15]
    }

    MIXED_REPLACE_PASSWORD_SUCCESSFUL = {
      "username": REG_USERNAME,
      "old_password": PASSWORD_TEMPLATE[:15],
      "password1": PASSWORD_TEMPLATE[3:21],
      "password2": PASSWORD_TEMPLATE[3:21]
    }

    MIXED_LOGIN_WITH_OLD_PASSWORD = {
      "username": REG_USERNAME,
      "password": PASSWORD_TEMPLATE[:15]
    }

    MIXED_LOGIN_WITH_NEW_PASSWORD = {
      "username": REG_USERNAME,
      "password": PASSWORD_TEMPLATE[3:21]
    }

    MIXED_TODO_SUCCESSFUL_CREATE = {
        "text": "create test todo",
        "status": "TODO"
    }

    MIXED_SECOND_REPLACE_PASSWORD_SUCCESSFUL = {
      "username": REG_USERNAME,
      "old_password": PASSWORD_TEMPLATE[3:21],
      "password1": PASSWORD_TEMPLATE[:15],
      "password2": PASSWORD_TEMPLATE[:15]
    }
