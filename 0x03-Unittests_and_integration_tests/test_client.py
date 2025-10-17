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
        """Test that GithubOrgClient.org returns correct value and calls get_json"""
        # 1️⃣ Set a dummy return value for the mock
        expected_payload = {'repos_url': f'https://api.github.com/orgs/{org_name}/repos'}
        mock_get_json.return_value = expected_payload

        # 2️⃣ Instantiate a fresh GithubOrgClient
        client = GithubOrgClient(org_name)

        # 3️⃣ Access the property to trigger get_json
        result = client.org

        # 4️⃣ Assert get_json called exactly once with correct URL
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )

        # 5️⃣ Assert the return value matches the mock
        self.assertEqual(result, expected_payload)
