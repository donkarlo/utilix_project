from typing import Union

class Email:
    '''
    This class responisbility is to hold the structure of an email
    '''
    def __init__(self, input_email: str):
        '''

        Args:
            input_email:str
        '''
        if not isinstance(input_email, str):
            raise TypeError("Invalid type. As an email string is expected")

        self._input_email = input_email
        self._refined = None

        self._parts: Union[dict, None] = None
        self._id: Union[str, None] = None
        self._domain: Union[str, None] = None

        self._set_parts()  # separate method, sets values

    def get_refined(self) -> str:
        '''

        Returns: str

        '''
        if self._refined is None:
            self._refined = self._input_email.lower()
        return self._refined

    def _set_parts(self):
        '''Fills in self._parts, self._id, and self._domain, or leaves them None.'''
        parts = self.get_refined().split('@')
        if len(parts) == 2:
            self._parts = {"id": parts[0], "domain": parts[1]}
            self._id = parts[0]
            self._domain = parts[1]
        else:
            self._parts = None
            self._id = None
            self._domain = None

    def get_id(self) -> Union[str, None]:
        return self._id

    def get_domain(self) -> Union[str, None]:
        return self._domain

    def get_parts(self) -> Union[dict, None]:
        return self._parts
