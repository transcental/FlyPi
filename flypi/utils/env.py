import os

from dotenv import load_dotenv

load_dotenv()


class Environment:
    def __init__(self):
        self.port = int(os.environ.get("PORT", 3000))
        self.asendia_api_key = os.environ.get("ASENDIA_API_KEY", "unset")
        self.environment = os.environ.get("ENVIRONMENT", "development")

        unset = [key for key, value in self.__dict__.items() if value == "unset"]

        if unset:
            raise ValueError(
                f"Missing environment variables: {', '.join(unset).upper()}"
            )


env = Environment()
