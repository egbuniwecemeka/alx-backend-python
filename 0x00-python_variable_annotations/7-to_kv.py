#!/usr/bin/python3

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    return (k, float(v) ** 2)
