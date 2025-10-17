#!/usr/bin/env python3
""" Test module for Github org client """

from unittest import TestCase
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized

class TestGithubOrgClient(TestCase):
    """ Tests GithubOrgClient """
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, test_org,  mock_get):
        """ Tests that GithubOrgClient.orrg returns the correct value """

        client = GithubOrgClient(test_org)
        result = client.org

        # Test
        mock_get.assert_called_once_with(f'https://api.github.com/orgs/{test_org}')
