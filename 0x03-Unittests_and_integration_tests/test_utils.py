#!/usr/bin/env python3
""" Unit test """

from unittest import TestCase
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json
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
    # creates new methods on the test
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    # decorates test_access_nested_map..., expanding its attributes
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b",))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        # check to see if test raises necessary KeyError
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
        
class TestGetJson(TestCase):
    """ Test get_json to check for expected result """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_data):
        # Mock data
        mock_result = Mock()
        mock_result.json.return_value = test_payload
        mock_data.return_data = mock_result

        # Retrieve data from test_url
        result = get_json(test_url)

        #
        mock_data.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
