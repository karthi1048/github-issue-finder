from models import Issue

class IssueFilter:
    """
    Filters issues based on predefined rules.
    """

    def apply_filters(self, issues: list[Issue]) -> list[Issue]:
        """
        Return only issues that pass all filters.
        """
        filtered = []
        for issue in issues:
            if self._is_assigned(issue):
                continue
            if self._is_pull_request(issue):
                continue

            filtered.append(issue)

        return filtered

    def _is_assigned(self, issue: Issue) -> bool:
        """
        Returns True if the issue already has an assignee.
        """
        return issue.assignee is not None

    def _is_pull_request(self, issue: Issue) -> bool:
        """
        Returns True if the item is actually a pull request.
        """
        return issue.is_pull_request