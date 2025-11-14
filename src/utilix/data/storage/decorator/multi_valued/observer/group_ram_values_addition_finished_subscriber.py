from typing import runtime_checkable, Protocol, Any
from utilix.data.storage.decorator.multi_valued.observer.add_to_ram_values_subscriber import AddToRamValuesSubscriber


@runtime_checkable
class GroupRamValuesAdditionFinishedSubscriber(Protocol):

    def do_when_group_ram_values_addition_is_finished(self)->None: ...