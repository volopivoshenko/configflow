"""Tests configuration."""

from pathlib import Path
from typing import Any
from typing import Dict

import pytest


@pytest.fixture(scope="module")
def expected_filepath() -> Path:
    """Get expected filepath."""

    return Path("tests/fixtures/example.yaml")


@pytest.fixture(scope="module")
def expected_content() -> Dict[str, Any]:
    """Get expected content."""

    return {
        "databases": {
            "postgres": {
                "user": "admin",
                "password": "admin",
                "host": "localhost",
                "port": 5432,
                "schema": "public",
            },
            "mysql": {
                "user": "admin",
                "password": "admin",
                "host": "localhost",
                "port": 5001,
                "schema": "PUBLIC",
            },
            "kafka": {
                "consumer": {
                    "bootstrap_servers": "localhost:9092",
                    "auto_offset_reset": "earliest",
                    "key_deserializer": "org.apache.kafka.common.serialization.StringDeserializer",
                    "value_deserializer": (
                        "org.apache.kafka.common.serialization.StringDeserializer"
                    ),
                },
                "producer": {
                    "bootstrap_servers": "localhost:9092",
                    "key_serializer": "org.apache.kafka.common.serialization.StringSerializer",
                    "value_serializer": "org.apache.kafka.common.serialization.StringSerializer",
                },
            },
        },
        "logger": {
            "formatters": {
                "default": {
                    "format": "%(asctime)s %(levelname)-8s %(name)-15s %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "level": "INFO",
                    "stream": "ext://sys.stdout",
                },
                "file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "formatter": "default",
                    "filename": "logconfig.log",
                    "max_bytes": 1024,
                    "backup_count": 3,
                },
            },
        },
    }
