#!/usr/bin/env python3
""" Unit test """

from unittest import TestCase
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize
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
    """ Test class for utis.access_nested_map """
    # creates new methods on the test
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map for corresponding key-value pairs """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    # decorates test_access_nested_map..., expanding its attributes
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b",))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test to check if test raises necessary KeyError """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """ Test utils.get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_data):
        """ Test that get_json returns the expected result """

        # Mock data
        mock_result = Mock()
        mock_result.json.return_value = test_payload
        mock_data.return_value = mock_result

        # Retrieve data from test_url
        result = get_json(test_url)

        # Assert that requests.get was called once with the right url
        mock_data.assert_called_once_with(test_url)

        # Assert that function returns the expected result.
        self.assertEqual(result, test_payload)


class TestMemoize(TestCase):
    """ Test memoize decorator """

    def test_memoize(self):
        """  Test that a_method is called once """

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Patch TestClass.a_method using context manager style content
        with patch.object(TestClass, 'a_method', return_value=42) as mock_data:
            obj = TestClass()

            # Call it twice
            result1 = obj.a_property
            result2 = obj.a_property

            # Assert call is correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_data.assert_called_once()
