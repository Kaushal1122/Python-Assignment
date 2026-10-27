
import logging
from contextlib import contextmanager

import mysql.connector
from mysql.connector import Error

from src.config import load_config

logger = logging.getLogger(__name__)


class DatabaseConnectionError(Exception):
    pass


@contextmanager
def get_connection():
    config = load_config()
    connection = None

    try:
        connection = mysql.connector.connect(
            host=config["host"],
            port=config["port"],
            database=config["database"],
            user=config["user"],
            password=config["password"],
        )

        logger.info("Database connection established.")
        yield connection

    except Error as exc:
        logger.exception("Database operation failed.")
        raise DatabaseConnectionError(
            "Unable to connect to or operate on the database."
        ) from exc

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            logger.info("Database connection closed.")
