
from contextlib import contextmanager
from unittest.mock import MagicMock

from src import record_generator


def test_generate_records_fetches_incrementally(monkeypatch):
    connection = MagicMock()
    cursor = MagicMock()
    cursor.fetchone.side_effect = [
        (1, "Alice"),
        (2, "Bob"),
        None,
    ]
    connection.cursor.return_value = cursor

    @contextmanager
    def fake_connection():
        yield connection

    monkeypatch.setattr(
        record_generator,
        "get_connection",
        fake_connection,
    )

    records = record_generator.generate_records(
        "SELECT id, name FROM employees WHERE id > %s",
        (0,),
    )

    assert next(records) == (1, "Alice")
    assert next(records) == (2, "Bob")
    assert next(records, None) is None

    cursor.execute.assert_called_once_with(
        "SELECT id, name FROM employees WHERE id > %s",
        (0,),
    )
    assert cursor.fetchone.call_count == 3
    cursor.close.assert_called_once()


def test_generator_closes_cursor_when_stopped_early(monkeypatch):
    connection = MagicMock()
    cursor = MagicMock()
    cursor.fetchone.return_value = (1, "Alice")
    connection.cursor.return_value = cursor

    @contextmanager
    def fake_connection():
        yield connection

    monkeypatch.setattr(
        record_generator,
        "get_connection",
        fake_connection,
    )

    records = record_generator.generate_records(
        "SELECT id, name FROM employees"
    )

    assert next(records) == (1, "Alice")

    records.close()

    cursor.close.assert_called_once()
