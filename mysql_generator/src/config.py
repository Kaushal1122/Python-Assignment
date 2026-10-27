
import configparser
import os
from pathlib import Path


class ConfigurationError(Exception):
    pass


def load_config():
    config_path = Path(__file__).resolve().parent.parent / "config.ini"

    parser = configparser.ConfigParser()

    if not config_path.is_file():
        raise ConfigurationError(
            f"Configuration file not found: {config_path}"
        )

    parser.read(config_path)

    try:
        host = parser.get("database", "host")
        port = parser.getint("database", "port")
        database = parser.get("database", "database")
        user = parser.get("database", "user")
        password = os.getenv("MYSQL_PASSWORD")
        batch_size = parser.getint("processing", "batch_size")
    except (configparser.Error, ValueError) as exc:
        raise ConfigurationError(
            "Invalid or missing configuration value."
        ) from exc

    if not password:
        raise ConfigurationError(
            "MYSQL_PASSWORD environment variable is not set."
        )

    if not 1 <= port <= 65535:
        raise ConfigurationError("Database port must be between 1 and 65535.")

    if batch_size <= 0:
        raise ConfigurationError("Batch size must be greater than zero.")

    return {
        "host": host,
        "port": port,
        "database": database,
        "user": user,
        "password": password,
        "batch_size": batch_size,
    }
