import logging
from unittest.mock import call, patch

from src.main import QUERIES, QUERY_PARAMS, main


def test_main_processes_all_records_and_prints_only_ten_per_query(
    capsys,
    caplog,
):
    records = [
        (i, f"First{i}", f"Last{i}")
        for i in range(1, 13)
    ]

    query_results = [
        iter(records)
        for _ in QUERIES
    ]

    with (
        patch(
            "src.main.generate_records",
            side_effect=query_results,
        ) as mock_generate,
        caplog.at_level(logging.INFO),
    ):
        result = main()

    output = capsys.readouterr()

    assert result == 0

    printed_records = [
        line
        for line in output.out.splitlines()
        if line.startswith("(")
    ]

    assert len(printed_records) == 70
    assert mock_generate.call_count == len(QUERIES)

    assert "Total records processed: 12" in caplog.text
    assert "All queries executed successfully." in caplog.text


def test_main_executes_all_queries_in_order():
    records = [
        iter([(1, "Alice", "Smith")])
        for _ in QUERIES
    ]

    expected_calls = [
        call(query, QUERY_PARAMS.get(title))
        for title, query in QUERIES.items()
    ]

    with patch(
        "src.main.generate_records",
        side_effect=records,
    ) as mock_generate:
        result = main()

    assert result == 0
    assert mock_generate.call_args_list == expected_calls
