#!/usr/bin/env python3
""" Unit test """

from unittest import TestCase
from utils import access_nested_map
from parameterized import parameterized

""" class parameterized:
    @staticmethod
    def expand(cases):
        def decorator(func):
            def wrapper(self):
                for case in cases:
                    with self.subTest(case=case):
                        result = func(self, *case)
                        return result
            return wrapper
        return decorator """

class TestAccessNestedMap(TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    # decorates test_access_nested_map, expanding its attributes
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b",))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        # check to see if test raises necessary KeyError
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)