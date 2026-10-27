from src.main import get_squares


def test_squares_from_one_to_twenty():
    expected = [num ** 2 for num in range(1, 21)]
    assert get_squares() == expected


def test_squares_count():
    assert len(get_squares()) == 20


def test_first_and_last_squares():
    result = get_squares()
    assert result[0] == 1
    assert result[-1] == 400