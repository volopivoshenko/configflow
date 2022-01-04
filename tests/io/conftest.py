"""Configuration for the tests."""

from pathlib import Path
from typing import Any
from typing import Dict

import pytest


@pytest.fixture(scope="module")
def dotenv_dictionary() -> Dict[Any, Any]:
    """Get dictionary example in the DOTENV format."""

    return {
        "DB_DB2_HOST": "localhost",
        "DB_DB2_PORT": 50000,
        "DB_POSTGRES_HOST": "localhost",
        "DB_POSTGRES_PORT": 8080,
        "API_SCHEMA": "rest",
        "API_AUTH": "basic",
    }


@pytest.fixture(scope="module")
def dotenv_stream() -> str:
    """Get dictionary representation in the DOTENV format."""

    return "\n".join(
        (
            "# databases config",
            "# IBM DB2",
            "DB_DB2_HOST=localhost",
            "DB_DB2_PORT=50000",
            "# Postgres",
            "DB_POSTGRES_HOST=localhost",
            "DB_POSTGRES_PORT=8080",
            "# API",
            "API_SCHEMA=rest",
            "API_AUTH=basic",
        ),
    )


@pytest.fixture
def dotenv_file(tmpdir: Path, dotenv_stream: str) -> Path:
    """Create and get example of the DOTENV file."""

    filepath = tmpdir / "example.env"
    with open(filepath, "w") as env_file:
        env_file.write(dotenv_stream)

    return filepath


@pytest.fixture(scope="module")
def ini_dictionary() -> Dict[Any, Any]:
    """Get dictionary example in the INI format."""

    return {
        "db.db2": {
            "host": "localhost",
            "port": 50000,
        },
        "db.postgres": {
            "host": "localhost",
            "port": 8080,
        },
        "api": {
            "schema": "rest",
            "auth": "basic",
        },
    }


@pytest.fixture(scope="module")
def ini_stream() -> str:
    """Get dictionary representation in the INI format."""

    return "\n".join(
        (
            "# database",
            "[db.db2]",
            "host = localhost",
            "port = 50000",
            "[db.postgres]",
            "host = localhost",
            "port = 8080",
            "# api",
            "[api]",
            "schema = rest",
            "auth = basic",
        ),
    )


@pytest.fixture
def ini_file(tmpdir: Path, ini_stream: str) -> Path:
    """Create and get example of the INI file."""

    filepath = tmpdir / "example.env"
    with open(filepath, "w") as ini_file:
        ini_file.write(ini_stream)

    return filepath
