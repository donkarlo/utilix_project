import pytest
from utilityx.network.internet.email.email_address import EmailAddress


class TestEmailAddress:

    @pytest.mark.parametrize(
        "input_email",
        [
            1,
            (1,3),
            {"email":1},
        ]
    )
    def test___init__(self, input_email:str):
        '''
        for all param values TypeError must be caught
        Args:
            input_email:

        Returns:

        '''
        with pytest.raises(TypeError) as exc_info:
            EmailAddress(input_email)  # Passing int should raise TypeError
        assert isinstance(exc_info.value, TypeError)

    def test_get_id_and_domain_for_valid_email(self):
        email = EmailAddress("mohammad.rahmani.xyz@gmail.com")
        assert email.get_id() == "mohammad.rahmani.xyz"
        assert email.get_domain() == "gmail.com"

    def test_refinement_lowers_case(self):
        email = EmailAddress("UPPER.CASE@DOMAIN.COM")
        assert email.get_refined() == "upper.case@domain.com"

    def test_get_id_domain_consistency(self):
        email = EmailAddress("a.b@x.y")
        assert email.get_id() == "a.b"
        assert email.get_domain() == "x.y"

    def test__get_parts_structure(self):
        email = EmailAddress("foo@bar.com")
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
        email = EmailAddress(input_email)
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
    def test_get_parts(self, input_email, expected_parts:dict[str, str]):
        '''

        Args:
            input_email(str): input email
            expected_parts(dict):
                - 'id' (str): the user part of the email
                - 'domain' (str): the domain part of the email

        Returns:

        '''
        email = EmailAddress(input_email)
        assert email.get_parts() == expected_parts
