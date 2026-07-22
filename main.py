from config import Config
from github_client import GitHubClient
from filters import IssueFilter
from scorer import IssueScorer

def main() -> None:
    config = Config()

    repositories = config.load_repositories()
    client = GitHubClient(config.github_token)
    issue_filter = IssueFilter()
    scorer = IssueScorer()
    print("\nScanning Repositories\n")

    # Listing repositories using enumerate for better readability and indexing.
    # for index, repository in enumerate(repositories, start=1):
    #     print(f"{index}. {repository}")

    for repository in repositories:
        issues = client.get_open_issues(repository)
        original_count = len(issues)
        filtered_issues = issue_filter.apply_filters(issues)
        scored_issues = scorer.score(filtered_issues)

        print(f"\nRepository: {repository}")
        print(f"Original Issues: {original_count}\n")
        print(f"Filtered Issues: {len(filtered_issues)}\n")
    
        for issue in scored_issues[:5]:  # Display only the first 5 issues
            print(f"[Score: {issue.score:>2}] #{issue.number} - {issue.title}")

        print("\n" + "-" * 40) # Separator for better readability between repositories

# Guard to ensure the main function runs only when the script is executed directly.
if __name__ == "__main__":
    main()