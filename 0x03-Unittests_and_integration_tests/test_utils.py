#!/usr/bin/env python3
""" Unit test """

from unittest import TestCase
from utils import access_nested_map

class parameterized:
    @staticmethod
    def expand(cases):
        def decorator(func):
            def wrapper(self):
                for case in cases:
                    with self.subTest(case=case):
                        result = func(self, *case)
                        return result
            return wrapper
        return decorator

class TestAccessNestedMap(TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
