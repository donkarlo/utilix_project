import string
from typing import Union
from utilityx.internet.email.email import Email


class Validator:
    def __init__(self, input_email:Union[str, Email]):
        self._input_email = input_email

        if isinstance(input_email, str):
            self._email = Email(input_email)
        elif isinstance(input_email, Email):
            self._email = input_email
        else:
            raise TypeError("Invalid type. Either string or Email is expected")

        #lazy loading
        self._validity = None
        self._error_msgs:list[str] = []

    def get_validity(self)->bool:
        if self._validity is None:
            self._validity = self._has_two_parts()
            self._validity &= self._has_allowed_symbols()
        return self._validity

    def _has_two_parts(self)->bool:
        if self._email.get_id() is not None and self._email.get_domain() is not None:
            return True
        return False

    def _has_allowed_symbols(self)->bool:
        allowed = set(string.ascii_lowercase + string.digits + '.-_')
        parts:dict = self._email.get_parts()
        for part_value in parts.values():
            if not set(part_value) <= allowed:
                return False
        return True

    def _add_error_msg(self, msg:str):
        self._error_msgs.append(msg)

    def get_error_msgs(self)->list[str]:
        return self._error_msgs

    def print_error_msgs(self):
        print(self._error_msgs)


