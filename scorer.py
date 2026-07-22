from models import Issue

class IssueScorer:
    """
    Calculates a score for GitHub issues.
    """

    LABEL_SCORES = {
        "good first issue": 10,
        "beginner": 8,
        "easy": 7,
        "help wanted": 5,
    }

    def score(self, issues: list[Issue]) -> list[Issue]:

        for issue in issues:
            issue.score = ( 
                self._label_score(issue) + self._comment_score(issue) 
            )

        return sorted(
            issues,
            key=lambda issue: issue.score, # For each Issue, use its score for sorting
            reverse=True,      # highest score first
        )

    # Calculate the score for an issue based on its labels
    def _label_score(self, issue: Issue) -> int:

        score = 0
        for label in issue.labels:
            score += self.LABEL_SCORES.get(label.lower(), 0)

        return score

    # Calculate the score for an issue based on its number of comments
    def _comment_score(self, issue: Issue) -> int:

        if issue.comments == 0:
            return 3
        if issue.comments <= 5:
            return 1
        if issue.comments > 15:
            return -3

        return 0