#!/usr/bin/env python3
""" Test module for Github org client """

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized

class TestGithubOrgClient(unittest.TestCase):
    """ Tests GithubOrgClient """

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, test_org, mock_get):
        """ Tests that GithubOrgClient.orrg returns the correct value """
        test_payload = {'repos_url': f'https://api.github.com/orgs/{test_org}/repos'}
        mock_get.return_value = test_payload

        client = GithubOrgClient(test_org)
        result = client.org

        # Test
        mock_get.assert_called_with(f'https://api.github.com/orgs/{test_org}')
        self.assertEqual(result, test_payload)

    def test_public_repos_url(self):
        """ Test for GithubOrgClient._public_repos_url """
        with patch.object(GithubOrgClient.org, new_callable=PropertyMock) as mock_payload:
            mock_payload.return_value = {'repos_url': 'http://api.github.com/orgs/testorg/repos'}
            
            # Result
            result = GithubOrgClient('testorg')._public_repos_url

            # Test
            self.assertEqual(result, 'http://api.github.com/orgs/testorg/repos')

