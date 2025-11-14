from typing import runtime_checkable, Protocol, Any

@runtime_checkable
class GroupRamValuesAdditionFinishedPublisher(Protocol):

    def attach_group_ram_values_finished_subscriber(self, add_values_finished_subscriber: GroupRamValuesAdditionFinishedSubscriber) -> None: ...

    def notify_group_ram_values_addition_finished_subscribers(self)->None: ...
