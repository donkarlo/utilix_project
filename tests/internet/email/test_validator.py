import pytest
from utilityx.internet.email.email import Email
from utilityx.internet.email.validator import Validator

class TestValidator:
    def test___init__(self):
        with pytest.raises(TypeError) as exc_info:
            Validator(1)  # Passing int should raise TypeError
        assert str(exc_info.value) == "Invalid type. Either string or Email is expected"

    def test_validity(self, shared_email_validator_object):
        assert shared_email_validator_object.get_validity() == True

    @pytest.mark.parametrize(
        "input_email, expected_result",
        [
            ("mo@ra.com", True),
            ("mohammadrahmani.xyz", False),
            ("a@b@c.com", False),
        ]
    )
    def test__has_two_parts(self, input_email, expected_result):
        assert Validator(input_email)._has_two_parts() == expected_result

    @pytest.mark.parametrize(
        "input_email, expected_result",
        [
            ("mo@ra.com", True),
            ("mohammadrah#mani.xyz", False),
            ("a@b@%c.com", False),
        ]
    )
    def test__has_has_allowed_symbols(self, input_email, expected_result):
        assert Validator(input_email)._has_two_parts() == expected_result
