import pytest

from utilityx.internet.email.concrete_email_address_validator import ConcereteEmailAddressValidator


@pytest.fixture
def shared_email_validator_object_with_valid_str_email():
    '''

    Returns:EmailAddressValidator

    '''
    return ConcereteEmailAddressValidator("mohammad.rahmani.xyz@gmail.com")

@pytest.fixture
def shared_email_address_object_with_valid_str_email():
    return ConcereteEmailAddressValidator("mohammad.rahmani.xyz@gmail.com")

@pytest.fixture
def conf_fixture():
    # load config file
    yield # test runs here
    # remove the config structure