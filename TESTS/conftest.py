import pytest
import sys
from API_Logic.PetFriends import PetFriends
from API_Logic.allure_logger import AllureLogger
from TESTS.settings import valid_password, valid_email
from TESTS.params import randomize_id
from API_Logic.DeletePet import dl


@pytest.fixture(scope="function")
def capture_console_output(request):
    """
    Fixture to capture console output (stdout and stderr)
    during a test and save it using AllureLogger.
    """
    test_name = request.node.name
    logger = AllureLogger(test_name)
    sys.stdout = logger
    sys.stderr = logger

    yield

    logger.save_logs_to_allure()


@pytest.fixture(scope="function")
def setup_key():
    """
    Fixture to set up a valid API key for testing.
    """
    pets_f = PetFriends()
    pets_f.get_api_key(valid_email, valid_password)
    header = {}
    header["auth_key"] = pets_f.auth_key["key"]
    yield header


@pytest.fixture(scope="function")
def setup_invalid_key():
    """
    Fixture to set up a valid API key for testing.
    """
    pets_f = PetFriends()
    pets_f.get_api_key(valid_email, valid_password)
    header = {}
    header["auth_key"] = "invalid_key"
    yield header


@pytest.fixture(scope="function")
def setup_invalid_id():
    """
    Fixture to set up an invalid pet ID for negative testing.
    """
    id = randomize_id()
    yield id


@pytest.fixture(scope="function")
def delete_pet_after():
    """
    Fixture to clean up after a test by deleting a pet.
    """
    pets_f = PetFriends()
    pets_f.get_api_key(valid_email, valid_password)
    header = {}
    header["auth_key"] = pets_f.auth_key["key"]

    yield header

    dl(header, None)



