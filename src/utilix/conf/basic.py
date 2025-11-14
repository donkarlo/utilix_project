from typing import Union, Any

from utilix.conf.interface import Interface as ConfInterface
from utilix.os.file_system.path.path import Path
from collections.abc import Hashable


class Basic(ConfInterface):
    '''
    to have a nested dictionary of key_values for configuaration
    '''
    _instance = None
    def __new__(cls, *args, **kwargs):
        '''Defines how __init__ should behave'''
        if cls._instance is None:
            #Go so high in hierarchy until you reach a class that has __new__ method overriden. in this case ABC doesnt have __new__ overriden so it calls objecy class __new__ method
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, source:str):
        '''
        to load the configs
        :param source:
        '''
        self._source = source

        #init
        self._props:Dict[str, Any] = None
        self._props()


    def get_prop(self, key:Union[list, str]):
        '''
        get just one property
        :param key: can be a str or a muti ['level1','level2',...] in first case this method retrns
        self._props[str] and in the second case self._props['level1']['level2']...
        :return:
        '''
        result = None
        if isinstance(key,str):
            result = self._props[key]
        elif isinstance(key,list):
            result = self._props
            for index in key:
                # Check if the current key exists in the dictionary
                if index in result:
                    # Update result to the raw_value corresponding to the current key
                    result = result[index]
                else:
                    raise KeyError(key)
        return result

    def get_props(self):
        '''
        get all properties
        :return:
        '''
        return self._props

    def get_source(self)->Path:
        return self._source

    def __call__(self, key:Union[list, str]=None):
        """
        Args:
            key: if the key is none then all _props are returned, if it is a flat muti then the related subtree is returned if it is str then the first level node is returned

        Returns:

        """
        if isinstance(key,None):
            return self._props
        elif isinstance(key,str):
            return self.get_prop(key)

    def __getitem__(self, key):
        """
        Args:
            key:

        Returns:

        """
        return self._props[key]

    def __setitem__(self, key:Hashable, value)->None:
        '''

        Args:
            key:
            value:

        Returns: None

        '''
        self._props[key] = value

    def __iter__(self)->Any:
        '''

        Returns:
        '''
        return iter(self._props)
