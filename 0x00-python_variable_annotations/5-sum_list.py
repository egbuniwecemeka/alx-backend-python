#!/usr/bin/env python3
"""A python script taking a list of floats and returns their sums (float)"""


def sum_list(input_list: list[float]) -> float:
    """Returns a list of float arguments """
    res: float = 0.0
    for val in input_list:
        res += val
    return res
