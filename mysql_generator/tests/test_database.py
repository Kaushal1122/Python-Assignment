
from unittest.mock import MagicMock

import mysql.connector
import pytest

from src.database import DatabaseConnectionError, get_connection


def test_connection_success(monkeypatch):
    connection = MagicMock()
    connection.is_connected.return_value = True

    monkeypatch.setattr(
        "src.database.load_config",
        lambda: {
            "host": "localhost",
            "port": 3306,
            "database": "employees",
            "user": "root",
            "password": "test_password",
            "batch_size": 1000,
        },
    )
    monkeypatch.setattr(
        "src.database.mysql.connector.connect",
        lambda **kwargs: connection,
    )

    with get_connection() as result:
        assert result is connection

    connection.close.assert_called_once()


def test_connection_failure(monkeypatch):
    monkeypatch.setattr(
        "src.database.load_config",
        lambda: {
            "host": "localhost",
            "port": 3306,
            "database": "employees",
            "user": "root",
            "password": "test_password",
            "batch_size": 1000,
        },
    )
    monkeypatch.setattr(
        "src.database.mysql.connector.connect",
        MagicMock(
            side_effect=mysql.connector.Error("Connection failed")
        ),
    )

    with pytest.raises(DatabaseConnectionError), get_connection():
        pass
