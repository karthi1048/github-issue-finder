from dataclasses import dataclass

@dataclass
class Issue:
    """
    Represents a GitHub Issue.
    """

    repository: str
    number: int
    title: str
    url: str
    labels: list[str]
    assignee: str | None
    comments: int