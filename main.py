from config import Config
from github_client import GitHubClient

def main() -> None:
    config = Config()

    repositories = config.load_repositories()
    client = GitHubClient(config.github_token)
    print("\nScanning Repositories\n")

    # Listing repositories using enumerate for better readability and indexing.
    # for index, repository in enumerate(repositories, start=1):
    #     print(f"{index}. {repository}")

    for repository in repositories:
        issues = client.get_open_issues(repository)
        print(f"\nRepository: {repository}")
        print(f"Open Issues: {len(issues)}\n")
    
        for issue in issues[:5]:  # Display only the first 5 issues
            print(f"Issue #{issue.number}: {issue.title}")

    # print(f"\nTotal repositories: {len(repositories)}")

# Guard to ensure the main function runs only when the script is executed directly.
if __name__ == "__main__":
    main()