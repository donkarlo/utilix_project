from enum import Enum
from beartype import beartype

class EmailStatus(Enum):
    SUCCESS = 0
    FAIL = 1
    NO_EMAIL_FOUND = 2
