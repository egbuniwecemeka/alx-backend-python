#!/usr/bin/env python3
""" Generic utility for github org client
"""
import requests
from functools import wraps
from typing import (Mapping,
                    Sequence,
                    Any,
                    Dict,
                    Callable,
)


__all__ = [
            "access_nested_map",
            "get_json",
            "memoize",
]

def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """ Access nested map with key path.
    Parameters
    ----------
    nested_map: Mapping
        A nested map
    path: Sequence
        A sequence of key representing a path to the value
    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -> Dict:
    """ Gets a response from a remote URL """
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """ Decorator to memoize a method.
    Example
    -------
    class MyClass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 42
    >>> my_object.a_method
    42
    """
    my_attr = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        if not hasattr(self, my_attr):
            setattr(self, my_attr, fn(self))
        return getattr(self, my_attr)
    return property(memoized)
