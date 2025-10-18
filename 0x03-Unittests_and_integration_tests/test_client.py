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
        test_payload = {
            'repos_url': f'https://api.github.com/orgs/{test_org}/repos'}
        mock_get.return_value = test_payload

        client = GithubOrgClient(test_org)
        result = client.org

        # Test
        mock_get.assert_called_with(f'https://api.github.com/orgs/{test_org}')
        self.assertEqual(result, test_payload)

    def test_public_repos_url(self):
        """ Test that GithubOrgClient._public_repos_url returns the right repos URL"""

        # Patch the org property on GithubOrgClient so it doesn't return the
        # real API
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_payload:
            # Set mock to return a fake organization dictionary
            mock_payload.return_value = {
                'repos_url': 'http://api.github.com/orgs/testorg/repos'}

            # Create a client instance and access thr _public_repos_url
            # property
            result = GithubOrgClient('testorg')._public_repos_url

            # Check that property returned the expected 'repos_url' value
            self.assertEqual(
                result, 'http://api.github.com/orgs/testorg/repos')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test GithubOrgClient.public_repos method """

        # Mock the return value of get_json for desired payload
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "org_license"}},
            {"name": "repo2", "license": {"key": "org_license"}}
        ]

        # Patch _public_repos_url property so it doesn't make a real API call
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_repos_url:
            # Simulate that the property returns a fake URL
            mock_repos_url.return_value = 'https://api.github.com/orgs/testorg/repos'

            # Create an instance of the client and call the method being tested
            client = GithubOrgClient('testorg')
            result = client.public_repos()

            # Confirm that the method returns a list of repos name as expected
            self.assertEqual(result, ['repo1', 'repo2'])

            # Check that get_son was called once with the mocked URL
            mock_get_json.assert_called_once_with(
                'https://api.github.com/orgs/testorg/repos')
