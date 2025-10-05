#!/usr/bin/env python3
""" Generic utility for github org client
"""

from functools import wraps
from typing import (Mapping,
                    Sequence,
                    Any)


__all__ = ["access_nested_map"]

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

if __name__ == "__main__":
    nested_map = {"a": {"b": {"c": 1}}}
    result = access_nested_map(nested_map, ["a", "b", "c"])
    print(result)