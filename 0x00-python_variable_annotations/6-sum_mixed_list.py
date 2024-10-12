#!/usr/bin/env python3
""" A python script annotating a list (floats/ints) into their sum (floats) """

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Returns mixed list values as a summed float"""
    res: float = 0.0
    for num in mxd_list:
        res += num
    return res
