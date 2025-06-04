from typing import Callable, Any, Sequence


class Mapx:
    def __init__(self):
        pass

    def get_maped_on_callable(self, seq:Sequence , lam:Callable[[Any], Any]):
        '''

        Args:
            lam: Callable[[Any], Any]

        Returns:

        '''
        return map(lam, seq)