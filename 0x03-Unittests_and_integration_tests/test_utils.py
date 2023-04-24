#!/usr/bin/env python3
"""
Module test_utils
"""
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test Class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests utils.access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
        ])
    def test_access_nested_map_exception(self, nested_map, path, err):
        """Tests utils.access_nested_map for KeyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path) == err


class TestGetJson(unittest.TestCase):
    """Test Class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """Tests with mock"""
        mock_requests_get.return_value.json.return_value = test_payload
        response = get_json(test_url)
        self.assertEqual(response, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test Class"""
    def test_memoize(self):
        """Tests memoize"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_obj:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_obj.assert_called_once()


if __name__ == '__main__':
    """Main entry"""
    unittest.main()
