import pytest
from sorting.insertion.insertion_sort import insertion_sort

def test_exists():
    assert insertion_sort()
def test_insertion_sort_1():
    actual = insertion_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_insertion_sort_2():
    actual = insertion_sort([-8, -4, 23, 42, 16, 15])
    expected = [-8, -4, 15, 16, 23, 42]
    assert actual == expected
