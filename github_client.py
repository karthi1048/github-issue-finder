import requests

class GitHubClient:
    """
    Client responsible for communicating with the GitHub REST API.
    """

    def __init__( self, token: str, base_url: str = "https://api.github.com" ) -> None:

        self.base_url = base_url
        self.session = requests.Session()
        # every request made with this session will include the Authorization header with the provided token.
        self.session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        )

    def _get(self, endpoint: str, params: dict | None = None):
        """
        Internal helper for GET requests.
        """

        url = f"{self.base_url}{endpoint}"

        response = self.session.get(
            url=url,
            params=params,
            timeout=30,
        )

        response.raise_for_status()
        return response.json()

    def get_open_issues(self, repository: str):
        """
        Fetch all open issues from a repository.
        """

        endpoint = f"/repos/{repository}/issues"

        params = {
            "state": "open",
        }

        return self._get(endpoint, params)