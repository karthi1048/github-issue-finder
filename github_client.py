import requests
from models import Issue

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

    # Conversion layer which knows GitHub's JSON structure.
    def _convert_issue(self, repository: str, data: dict) -> Issue:
        """
        Convert GitHub JSON into an Issue object.
        """

        # Using list comprehension to only extract label names & use get() to avoid KeyError if "labels" key is missing.
        labels = [
            label["name"]
            for label in data.get("labels", [])
        ]

        assignee = None

        # Check if the issue has an assignee and extract the login name if present.
        if data.get("assignee"):
            assignee = data["assignee"]["login"]

        # Returns an Issue object.
        return Issue(
            repository=repository,
            number=data["number"],
            title=data["title"],
            url=data["html_url"],
            labels=labels,
            assignee=assignee,
            comments=data["comments"],
        )

    def get_open_issues(self, repository: str):
        """
        Fetch all open issues from a repository.
        """

        endpoint = f"/repos/{repository}/issues"

        params = {
            "state": "open",
        }

        issues = self._get(endpoint, params)

        return [
            self._convert_issue(repository, issue)
            for issue in issues
        ]