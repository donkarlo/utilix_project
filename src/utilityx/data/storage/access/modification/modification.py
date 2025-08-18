from utilityx.data.storage.basic import RoleSet


class Modification:
    """
    Not very useful until each role needs more property and methods
    """
    def __init__(self, role:RoleSet):
        self._role = role
