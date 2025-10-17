#!/usr/bin/env python3
""" Test module for Github org client """

from unittest import TestCase
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized

class TestGithubOrgClient(TestCase):
    """Unit tests for GithubOrgClient"""

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json):
        """Test GithubOrgClient._public_repos_url property"""
        test_payload = {"repos_url": "https://api.github.com/orgs/testorg/repos"}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient("testorg")
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload
            self.assertEqual(client._public_repos_url, test_payload["repos_url"])
