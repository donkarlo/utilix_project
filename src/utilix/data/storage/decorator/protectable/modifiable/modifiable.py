from utilix.data.storage.decorator.protected.modificationed.role.core.kind import Kinds


class Modifiable:
    """
    Not very useful until each role needs more property and methods
    """
    def __init__(self, permitted_roles:Kinds):
        """
        TODO other modificationes will be added later
        :param roleSet:
        """
        self._permitted_roles = permitted_roles
