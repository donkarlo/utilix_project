import pytest
from utilityx.internet.email.email import Email

# @pytest.fixture
# def get_sample_email():
#     return Email("mohammad.rahmani.xyz@gmail.com")


class TestEmail:
    def test_get_id_and_domain_for_valid_email(self):
        email = Email("mohammad.rahmani.xyz@gmail.com")
        assert email.get_id() == "mohammad.rahmani.xyz"
        assert email.get_domain() == "gmail.com"

    def test_refinement_lowers_case(self):
        email = Email("UPPER.CASE@DOMAIN.COM")
        assert email.get_refined() == "upper.case@domain.com"

    def test_get_id_domain_consistency(self):
        email = Email("a.b@x.y")
        assert email.get_id() == "a. b"
        assert email.get_domain() == "x.y"

    def test__get_parts_structure(self):
        email = Email("foo@bar.com")
        parts = email.get_parts()
        assert parts == {"id": "foo", "domain": "bar.com"}

    @pytest.mark.parametrize(
        "input_email, expected_id, expected_domain",
        [
            ("foo@bar.com", "foo", "bar.com"),
            ("UPPER@CASE.COM", "upper", "case.com"),
            ("user.name@host.co.uk", "user.name", "host.co.uk"),
            ("user.test", None, None)
        ]
    )
    def test_parsing_multiple_emails(self, input_email, expected_id, expected_domain):
        email = Email(input_email)
        assert email.get_id() == expected_id
        assert email.get_domain() == expected_domain

    @pytest.mark.parametrize(
        "input_email, expected_parts",
        [
            ("foo@bar.com", {"id":"foo", "domain":"bar.com"}),
            ("UPPER@CASE.COM", {"id":"upper", "domain":"case.com"}),
            ("user.name@host.co.uk", {"id":"user.name", "domain":"host.co.uk"}),
            ("user.test", None)
        ]
    )
    def test_get_parts(self, input_email, expected_parts:dict):
        email = Email(input_email)
        assert email.get_parts() == expected_parts
