from typing import Union
from utilityx.internet.email.email_address import EmailAddress
from beartype import beartype

from utilityx.internet.email.email_status import EmailStatus


class Email:
    def __init__(self,
                 sender: Union[EmailAddress, str],
                 recievers: list[Union[EmailAddress, str], ...],
                 body: str,
                 email_status: int):
        '''

        Args:
            sender (Union[EmailAddress, str]):
            recievers:
            body:
            email_status:
        '''
        # checks
        if email_status not in {e.value for e in EmailStatus}:
            raise ValueError(f"Invalid email_status: {email_status}. Must be one of {[e.value for e in EmailStatus]}.")

        #assignment
        self._sender = sender
        self._recievers = recievers
        self._body = body
        self._email_status = email_status