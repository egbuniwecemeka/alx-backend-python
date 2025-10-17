#!/usr/bin/env python3
"""Test module for GithubOrgClient"""

from unittest import TestCase
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(TestCase):
    """Tests GithubOrgClient"""

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org calls get_json with correct URL"""
        # Give the mock a simple dictionary so no errors occur
        mock_get_json.return_value = {'repos_url': f'https://api.github.com/orgs/{org_name}/repos'}

        # Fresh instance for each parameter
        client = GithubOrgClient(org_name)

        # Access the property to trigger get_json
        _ = client.org

        # Check that get_json was called exactly once with the correct URL
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )
