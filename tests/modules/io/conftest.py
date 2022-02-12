"""Configuration of the tests."""

from typing import Any
from typing import Dict

import pytest


@pytest.fixture(scope="module")
def expected_ini_dict() -> Dict[str, Any]:
    """Get the expected dictionary - content of the fixture files."""

    return {
        "databases.postgres": {
            "user": "admin",
            "password": "admin",
            "host": "localhost",
            "port": 5432,
            "schema": "public",
        },
        "databases.mysql": {
            "user": "admin",
            "password": "admin",
            "host": "localhost",
            "port": 5001,
            "schema": "PUBLIC",
        },
        "databases.kafka.consumer": {
            "bootstrap_servers": "localhost:9092",
            "auto_offset_reset": "earliest",
            "key_deserializer": "org.apache.kafka.common.serialization.StringDeserializer",
            "value_deserializer": "org.apache.kafka.common.serialization.StringDeserializer",
        },
        "databases.kafka.producer": {
            "bootstrap_servers": "localhost:9092",
            "key_serializer": "org.apache.kafka.common.serialization.StringSerializer",
            "value_serializer": "org.apache.kafka.common.serialization.StringSerializer",
        },
        "logger.formatters.default": {
            "format": "%(asctime)s %(levelname)-8s %(name)-15s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "logger.handlers.console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",
            "stream": "ext://sys.stdout",
        },
        "logger.handlers.file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": "logconfig.log",
            "max_bytes": 1024,
            "backup_count": 3,
        },
    }


@pytest.fixture(scope="module")
def expected_dotenv_dict() -> Dict[str, Any]:
    """Get the expected dictionary - content of the fixture files."""

    return {
        "DATABASES.POSTGRES.USER": "admin",
        "DATABASES.POSTGRES.PASSWORD": "admin",
        "DATABASES.POSTGRES.HOST": "localhost",
        "DATABASES.POSTGRES.PORT": 5432,
        "DATABASES.POSTGRES.SCHEMA": "public",
        "DATABASES.MYSQL.USER": "admin",
        "DATABASES.MYSQL.PASSWORD": "admin",
        "DATABASES.MYSQL.HOST": "localhost",
        "DATABASES.MYSQL.PORT": 5001,
        "DATABASES.MYSQL.SCHEMA": "public",
        "DATABASES.KAFKA.CONSUMER.BOOTSTRAP_SERVERS": "localhost:9092",
        "DATABASES.KAFKA.CONSUMER.AUTO_OFFSET_RESET": "earliest",
        "DATABASES.KAFKA.CONSUMER.KEY_DESERIALIZER": (
            "org.apache.kafka.common.serialization.StringDeserializer"
        ),
        "DATABASES.KAFKA.CONSUMER.VALUE_DESERIALIZER": (
            "org.apache.kafka.common.serialization.StringDeserializer"
        ),
        "DATABASES.KAFKA.PRODUCER.BOOTSTRAP_SERVERS": "localhost:9092",
        "DATABASES.KAFKA.PRODUCER.KEY_DESERIALIZER": (
            "org.apache.kafka.common.serialization.StringDeserializer"
        ),
        "DATABASES.KAFKA.PRODUCER.VALUE_DESERIALIZER": (
            "org.apache.kafka.common.serialization.StringDeserializer"
        ),
        "LOGGER.FORMATTERS.DEFAULT.FORMAT": "%(asctime)s %(levelname)-8s %(name)-15s %(message)s",
        "LOGGER.FORMATTERS.DEFAULT.DATEFMT": "%Y-%m-%d %H:%M:%S",
        "LOGGER.HANDLERS.CONSOLE.CLASS": "logging.StreamHandler",
        "LOGGER.HANDLERS.CONSOLE.FORMATTER": "default",
        "LOGGER.HANDLERS.CONSOLE.LEVEL": "INFO",
        "LOGGER.HANDLERS.CONSOLE.STREAM": "ext://sys.stdout",
        "LOGGER.HANDLERS.FILE.CLASS": "logging.handlers.RotatingFileHandler",
        "LOGGER.HANDLERS.FILE.FORMATTER": "default",
        "LOGGER.HANDLERS.FILE.FILENAME": "logconfig.log",
        "LOGGER.HANDLERS.FILE.MAX_BYTES": 1024,
        "LOGGER.HANDLERS.FILE.BACKUP_COUNT": 3,
    }


@pytest.fixture(scope="module")
def expected_yaml_dict() -> Dict[str, Any]:
    """Get the expected dictionary - content of the fixture files."""

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