from unittest.mock import patch

from src.general_example import GeneralExample

def test_flatten_dictionary():
    content = {
        "key1": [3, 2, 1],
        "key2": [42, 55, 10],
        "key3": [0, 22],
    }

    assert GeneralExample.flatten_dictionary(content) == [
        0, 1, 2, 3, 10, 22, 42, 55
        ]

def test_flatten_dictionary_removes_duplicates():
    content = {"key1": [1, 2, 2], "key2": [2, 3, 3]}

    assert GeneralExample.flatten_dictionary(content) == [1, 2, 3]

def test_flatten_dictionary_empty():
    assert GeneralExample.flatten_dictionary({}) == []


def test_fetch_emp_details():
    example = GeneralExample()

    with patch.object(
        example,
        "load_employee_rec_from_database",
        return_value=["emp001", "Sam", "100000"],
    ) as mock_load:
        result = example.fetch_emp_details()

    assert result == {
        "empId": "emp001",
        "empName": "Sam",
        "empSalary": "100000",
    }
    mock_load.assert_called_once_with()