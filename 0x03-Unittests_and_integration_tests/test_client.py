#!/usr/bin/env python3
""" Test module for Github org client """

from unittest import TestCase
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized

class TestGithubOrgClient(TestCase):
    """ Tests GithubOrgClient """
    @parameterized.expand([
        ('google', {'org_payload': True}),
        ('abc', {'org_payload': False}),
    ])
    @patch('client.get_json')
    def test_org(self, test_org, test_payload,  mock_get):
        """ Tests that GithubOrgClient.orrg returns the correct value """
        mock_result = Mock()
        mock_result.json.return_value = test_payload
        mock_get.return_value = mock_result

        client = GithubOrgClient(test_org)
        result = client.org

        # Test
        mock_get.assert_called_once_with(f'https://api.github.com/{test_org}')
        self.assertEqual(result, test_payload)
