#!/usr/bin/env python3
""" """
from typing import (Dict, List)
from utils import (access_nested_map, get_json, memoize,)

class GithubOrgClient:
    """ Github org class """
    
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_url) -> None:
        """ Instantiate """
        self._org_url = org_url

    @memoize
    def org(self) -> Dict:
        """ """
        return get_json(self.ORG_URL.format(org=self._org_url))
    
    @property
    def _public_repos_url(self) -> str:
        """  """
        return self.org['repos_url']

    @memoize
    def repos_payload(self) -> Dict:
        return get_json(self._public_repos_url)
    
    def public_repos(self, license: str = None) -> List[str]:
        """ """
        repo_payload = self.repos_payload
        public_repos_url = [
            repo['name'] for repo in repo_payload
            if license is None or self.has_license(repo, license)
        ]
        return public_repos_url
    
    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """ """
        assert license_key is not None, "license_key must not be None"
        try:
            has_license = access_nested_map(repo, ('license', 'key')) == license_key
        except KeyError:
            return False
        return has_license
    
        
if __name__ == "__main__":
    github = GithubOrgClient('facebook')
    print(github._public_repos_url)
    print(github.org)
    print(github.public_repos('mit'))
