
import logging
from unittest.mock import patch

from src.main import main


def test_main_processes_all_records_and_prints_only_ten(capsys, caplog):
    records = [
        (i, f"First{i}", f"Last{i}")
        for i in range(1, 13)
    ]

    with (
        patch("src.main.generate_records", return_value=iter(records)),
        caplog.at_level(logging.INFO),
    ):
        result = main()

    output = capsys.readouterr()

    assert result == 0
    assert len(output.out.strip().splitlines()) == 10
    assert "Total records processed: 12" in caplog.text
