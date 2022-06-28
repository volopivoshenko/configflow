"""Tests configuration."""

import typing

import pytest


DictType = typing.Dict[str, typing.Any]


@pytest.fixture(scope="module")
def expected_ini_dict() -> DictType:
    """Get the expected dictionary - content of the fixture file."""

    return {
        "databases.postgres": {
            "user": "admin",
            "password": "admin",
            "host": "localhost",
            "port": "5432",
            "schema": "public",
        },
        "databases.mysql": {
            "user": "admin",
            "password": "admin",
            "host": "localhost",
            "port": "5001",
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
            "max_bytes": "1024",
            "backup_count": "3",
        },
    }


@pytest.fixture(scope="module")
def expected_dotenv_dict() -> DictType:
    """Get the expected dictionary - content of the fixture file."""

    return {
        "DATABASES.POSTGRES.USER": "admin",
        "DATABASES.POSTGRES.PASSWORD": "admin",
        "DATABASES.POSTGRES.HOST": "localhost",
        "DATABASES.POSTGRES.PORT": "5432",
        "DATABASES.POSTGRES.SCHEMA": "public",
        "DATABASES.MYSQL.USER": "admin",
        "DATABASES.MYSQL.PASSWORD": "admin",
        "DATABASES.MYSQL.HOST": "localhost",
        "DATABASES.MYSQL.PORT": "5001",
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
        "LOGGER.HANDLERS.FILE.MAX_BYTES": "1024",
        "LOGGER.HANDLERS.FILE.BACKUP_COUNT": "3",
    }


@pytest.fixture(scope="module")
def expected_yaml_dict() -> DictType:
    """Get the expected dictionary - content of the fixture file."""

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


@pytest.fixture(scope="module")
def expected_properties_dict() -> DictType:
    """Get the expected dictionary - content of the fixture file."""

    return {
        "databases.kafka.consumer.auto_offset_reset": "earliest",
        "databases.kafka.consumer.bootstrap_servers": "localhost:9092",
        "databases.kafka.consumer.key_deserializer": (
            "org.apache.kafka.common.serialization.StringDeserializer"
        ),
        "databases.kafka.consumer.value_deserializer": (
            "org.apache.kafka.common.serialization.StringDeserializer"
        ),
        "databases.kafka.producer.bootstrap_servers": "localhost:9092",
        "databases.kafka.producer.key_deserializer": (
            "org.apache.kafka.common.serialization.StringDeserializer"
        ),
        "databases.kafka.producer.value_deserializer": (
            "org.apache.kafka.common.serialization.StringDeserializer"
        ),
        "databases.mysql.host": "localhost",
        "databases.mysql.password": "admin",
        "databases.mysql.port": "5001",
        "databases.mysql.schema": "public",
        "databases.mysql.user": "admin",
        "databases.postgres.host": "localhost",
        "databases.postgres.password": "admin",
        "databases.postgres.port": "5432",
        "databases.postgres.schema": "public",
        "databases.postgres.user": "admin",
        "logger.formatters.default.datefmt": "%Y-%m-%d %H:%M:%S",
        "logger.formatters.default.format": "%(asctime)s %(levelname)-8s %(name)-15s %(message)s",
        "logger.handlers.console.class": "logging.StreamHandler",
        "logger.handlers.console.formatter": "default",
        "logger.handlers.console.level": "INFO",
        "logger.handlers.console.stream": "ext://sys.stdout",
        "logger.handlers.file.backup_count": "3",
        "logger.handlers.file.class": "logging.handlers.RotatingFileHandler",
        "logger.handlers.file.filename": "logconfig.log",
        "logger.handlers.file.formatter": "default",
        "logger.handlers.file.max_bytes": "1024",
    }
