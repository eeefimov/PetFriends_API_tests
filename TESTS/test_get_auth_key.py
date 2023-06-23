from main import PetFriends
import pytest
from params import params_auth_positive, params_auth_negative

pets = PetFriends()

"""PRECONDITION: registered user with data: email, password"""

"""get auth key, valid user data(email, pass)"""
@pytest.mark.parametrize("email, password, expect", params_auth_positive,
                         ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_get_api_key_valid(email, password, expect):
    status, result = pets.get_api_key(email, password)
    assert status == expect
    if status == expect:
        assert "key" in pets.auth_key
    print("\n", pets.header)
    print(pets.auth_key)
    print(status)


"""invalid user data(email, pass)"""
@pytest.mark.parametrize("email, password, expect", params_auth_negative,
                         ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_get_api_key_invalid(email, password, expect):
    status, auth_key = pets.get_api_key(email, password)
    assert status == expect
    print("\n", pets.header)
    print(pets.auth_key)
    print(status)

