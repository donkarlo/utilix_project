import pytest
from utilityx.internet.email.validator import Validator
from utilityx.conf.file_config_loader import FileConfigLoader


@pytest.fixture
def shared_email_validator_object():
    return Validator("mohammad.rahmani.xyz@gmail.com")

@pytest.fixture
def conf_fixture():
    # load config file
    yield # test runs here
    # remove the config structure