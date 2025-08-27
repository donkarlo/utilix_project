from utilityx.data.storage.decorator.protected.modification.permitted_roles import PermittedRoles


class Modification:
    """
    Not very useful until each role needs more property and methods
    """
    def __init__(self, permitted_roles:PermittedRoles):
        """
        TODO other modificationes will be added later
        :param roleSet:
        """
        self._permitted_roles = permitted_roles
