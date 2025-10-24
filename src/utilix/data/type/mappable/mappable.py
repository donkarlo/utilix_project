from typing import Protocol, Type


class Mappable(Protocol):
    convertable_data_types: List[Type]
    def get_converted(self, conversion_data_type: Type) -> Type: ...

    def init_from_data_type_value(self, value:Type): ...