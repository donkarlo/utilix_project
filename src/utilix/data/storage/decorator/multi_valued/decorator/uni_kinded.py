from typing import Any
from utilix.data.storage.decorator.decorator import Decorator
from utilix.data.storage.decorator.multi_valued.multi_valued import MultiValued
from utilix.oop.inheritance.overriding.override_from import override_from

class UniKinded(Decorator):
    """
    - Uni formated means all documents in the same file or storage have the same format. for example  a a file full of many yaml documents
    - This meaningful only for sliced_value units
    - To check each raw_value to have the same group kind as other units.
    """
    def __init__(self, inner:MultiValued, expected_kind:type, validate_kind:bool):
        """

        Args:
            inner:
            expected_kind:
            validate_kind:
        """
        # to make sure that the units match
        if not isinstance(inner, MultiValued):
            raise TypeError(f"UniKinded requires a MultiValued, got {type(inner).__name__}")
        Decorator.__init__(self, inner)
        self._expected_kind = expected_kind
        self._validate_kind = validate_kind

    @override_from(Decorator)
    def save(self) -> None:
        # since Sliced MultiValue Storage is Iterable, then this will pass fine TODO: But is it the right way?
        if self._validate_kind == True:
            for counter, value in enumerate(self.get_ram()):
                if not isinstance(value, self._expected_kind):
                    raise ValueError(f"value #{counter} is not valid kind for the specified format. We need {self._expected_kind.__name__} but {type(value)} is given")
        #it actually runs the inner save
        Decorator.save(self)

    def add_to_ram(self, value:Any)->None:
        if self._validate_kind == True:
            if not isinstance(value, self._expected_kind):
                raise ValueError(
                    f"value {str(value)} is not valid kind for the specified format. We need {self._expected_kind.__name__} but {type(value)} is given")
        self._inner.add_to_ram(value)

