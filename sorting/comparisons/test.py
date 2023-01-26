import pytest
from sorting.comparisons.comparisons_sort import sort_by_recent_year, sort_by_title_alphabetically, movies


def test_exists_one():
    assert sort_by_recent_year()


def test_exists_two():
    assert sort_by_title_alphabetically()


def test_sort_by_recent_year():
    actual = sort_by_recent_year(movies)
    # Expected test output of test #1
    expected = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]
    assert actual == expected


def test_sort_by_title_alphabetically():
    actual = sort_by_title_alphabetically(movies)
    # Expected test output of test #2
    expected = ["Beetlejuice", "City of God", "Cotton Club", "Crocodile Dundee", "Intouchables", "Memento", "Ratatouille", "Shawshank Redemption", "Stardust", "Valkyrie"];
    assert actual == expected
