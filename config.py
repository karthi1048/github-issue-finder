from pathlib import Path
from dotenv import load_dotenv
import os

class Config:
    """
    Handles application configuration.
    Responsible for loading repositories from the configuration file.
    """

    # Methods utilize type hints for better code clarity and maintainability. 

    def __init__( self, repositories_file: str = "repositories.txt", env_file: str = ".env" ) -> None:
        self.repositories_file = Path(repositories_file)
        self.env_file = Path(env_file)

        load_dotenv(self.env_file)
        self.github_token = os.getenv("GITHUB_TOKEN")

        if not self.github_token:
            raise ValueError("GitHub token not found. Please set GITHUB_TOKEN in your .env file.")

    def load_repositories(self) -> list[str]:
        """
        Reads repositories from the repositories.txt file.
        Returns - list[str]: List of GitHub repositories in owner/repository format.
        Raises - FileNotFoundError: If repositories.txt does not exist.
        """

        if not self.repositories_file.exists():
            raise FileNotFoundError(
                f"Repository file '{self.repositories_file}' not found."
            )

        repositories = []

        with self.repositories_file.open("r", encoding="utf-8") as file:
            for line in file:
                repo = line.strip()

                if repo:
                    repositories.append(repo)

        return repositories