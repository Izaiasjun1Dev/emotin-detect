import os
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import Field
import yaml


class Settings(BaseSettings):
    openai_api_key: str = Field(
        default="",
    )
    openai_model: str = Field(
        default="gpt-4o-mini",
    )

    prompt_template: str = Field(
        default="você deve detectar as emoçoes contidas na {message} de"
        " acordo com as {format_instructions} e deve ser em portugues brasileiro",
    )

    @classmethod
    def from_yaml(cls, file_path: str):
        """
        Load settings from a YAML file.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        return cls(**data)

    @classmethod
    def from_env_yaml(cls, filename: str = ".env.yaml"):
        """
        Load settings from a YAML file located at the project root.
        If the file does not exist, fallback to default settings.
        """
        root_path = Path(__file__).parent.parent.parent.resolve()
        env_yaml_path = root_path / filename
        if env_yaml_path.exists():
            with open(env_yaml_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file) or {}
            return cls(**data)
        else:
            return cls()


# Prefer loading from .env.yaml at project root for textual configs like prompt templates
settings = Settings.from_env_yaml()
