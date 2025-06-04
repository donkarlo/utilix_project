from typing import Union

from utilityx.internet.email.email_address import EmailAddress
from utilityx.internet.email.email_status import EmailStatus
from beartype import beartype

from utilityx.internet.email.email import Email


class Inbox:
    def __init__(self, sender_email_address:EmailAddress, emails:list[Email,...]):
        '''

        Args:
            sender_email_address:
            emails: all single communications
        '''
        self._sender_email_address = sender_email_address
        self._single_communication = emails