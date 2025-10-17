from robotix.physical.brain.neuron import Neuron
from typing import Dict, Type, Any
class SmartFactory:
    def __init__(self, dic: Dict ,allowed_classes:List[Type]):
        """

        Args:
            dic:
            allowed_classes: class names such as Pose, Distribution, ...
        """
        pass



    def get_object(self, dic:Dict) -> Any:
        pass