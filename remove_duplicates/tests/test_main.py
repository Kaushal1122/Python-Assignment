from src.main import remove_duplicates


def test_remove_duplicates_preserves_order():
    numbers = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    assert remove_duplicates(numbers) == [12, 24, 35, 88, 120, 155]


def test_empty_list():
    assert remove_duplicates([]) == []


def test_all_unique_values():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_all_duplicate_values():
    assert remove_duplicates([5, 5, 5]) == [5]