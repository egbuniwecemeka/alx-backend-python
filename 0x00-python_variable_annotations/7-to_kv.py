#!/usr/bin/env python3
""" A pythons script of string and int/float tuple annotations"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple, of a string and an int or float"""
    return (k, float(v) ** 2)
