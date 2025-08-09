from typing import Union

from beartype import beartype

from utilityx.network.internet.email.email_address_validator import EmailAddressValidator
from utilityx.network.internet.email.email_address import EmailAddress


class ConcereteEmailAddressValidator(EmailAddressValidator):
    def __init__(self, email_address:Union[str,EmailAddress]):
        super().__init__(email_address)


    def _do_get_validity(self) ->bool:
        return True