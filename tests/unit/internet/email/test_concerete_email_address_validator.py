import pytest
from utilix.net.internet.email.concrete_email_address_validator import ConcereteEmailAddressValidator
class TestConcereteEmailAddressValidator:
    @pytest.mark.parametrize(
        "input_email",
        [
            1,
            (1, 3),
            {"email": 1},
        ]
    )
    def test___init__(self , input_email) -> None:
        with pytest.raises(TypeError) as exc_info:
            ConcereteEmailAddressValidator(input_email)  # Passing int should raise TypeError
        assert isinstance(exc_info.value, TypeError)

    def test_validity(self, shared_email_validator_object_with_valid_str_email) -> None:
        assert shared_email_validator_object_with_valid_str_email.get_validity() == True

    @pytest.mark.parametrize(
        "input_email, expected_result",
        [
            ("mo@ra.com", True),
            ("mohammadrahmani.xyz", False),
            ("a@b@c.com", False),
        ]
    )
    def test__has_two_parts(self, input_email, expected_result) -> None:
        assert ConcereteEmailAddressValidator(input_email)._has_two_parts() == expected_result

    @pytest.mark.parametrize(
        "input_email, expected_result",
        [
            ("mo@ra.com", True),
            ("mohammadrah#mani.xyz", False),
            ("a@b@%c.com", False),
        ]
    )
    def test__has_has_allowed_symbols(self, input_email, expected_result) -> None:
        assert ConcereteEmailAddressValidator(input_email)._has_two_parts() == expected_result
