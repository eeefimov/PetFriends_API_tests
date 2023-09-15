import allure
import pytest
from TESTS.settings import valid_email
from API_Logic.GetKey import PetFriendsGetKey
from TESTS.params import params_auth_positive, params_auth_negative

pf = PetFriendsGetKey()


@allure.feature("Get API Key")
@allure.suite("Get API Key")
class TestGetApiKey:

    @allure.title("Get API key using valid user values")
    @allure.description("""
    Get API Key using valid user values as: password, email.

    Precondition:
    - User successfully registered with a valid password and email.

    Expected result:
    - Get API key which should be used for other API methods.
    """)
    @pytest.mark.parametrize("email, password, expect", params_auth_positive,
                             ids=lambda val: f"{val} ({pytest.current_test_name()})")
    def test_get_api_key_valid(self, email, password, expect):
        status, result = pf.get_api_key(email, password)
        assert status == expect
        if status == 200:
            assert "key" in pf.auth_key

    @allure.title("Get API key using invalid user values")
    @allure.description("""
    Get API Key using invalid user values as: password, email.

    Precondition:
    - User uses invalid email and password, empty fields, or empty password field.

    Expected result:
    - Response returns error code 403.
    """)
    @pytest.mark.parametrize("email, password, expect", params_auth_negative,
                             ids=lambda val: f"{val} ({pytest.current_test_name()})")
    def test_get_api_key_invalid(self, email, password, expect):
        status, result = pf.get_api_key(email, password)
        assert status == expect


