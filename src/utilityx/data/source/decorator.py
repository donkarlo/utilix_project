from utilityx.data.format.supporting_format import SupportingFormat
from utilityx.data.source.interface import Source


class SourceDecorator(Source):
    def __init__(self, inner: Source):
        """
        Args:
            inner: The inner object to be decorated
        """
        self._inner:Source = inner

    def load_content(self)->str:
        """to set self._loaded_str_content"""
        self._inner.load_content()

    def save_content(self)->bool:
        """
        saves self._content
        No validity check will be performed here. Just the given string will be added
        Returns: success
        """
        self._inner.load_content()

    def add_to_content(self, content:str)->bool:
        self._content += content

    def __getattr__(self, name):
        target = self._inner
        while True:
            if hasattr(target, name):
                return getattr(target, name)
            elif hasattr(target, "_inner"):
                target = target._inner
            else:
                raise AttributeError(f"'{type(self).__name__}' and its inner chain have no attribute '{name}'")





