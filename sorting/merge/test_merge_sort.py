from sorting.merge.merge_sort import merge_sort

def test_exists():
    assert merge_sort()

def test_merge_sort_1():
    actual = merge_sort([8,4,23,42,16,15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_merge_sort_2():
    actual = merge_sort([5, 12, 7, 5, 5, 7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_merge_sort_2():
    actual = merge_sort([2, 3, 5, 7, 13, 11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected

