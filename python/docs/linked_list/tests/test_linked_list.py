import pytest
from linked_list.linked_list import Linked_List


def test_exists():
    assert Linked_List


def test_instantiate_linked_list():
    assert Linked_List()


def test_insert_linked_list():
    pass


def test_head():
    linked = Linked_List()
    assert linked.head is None


def test_insert_multiple_nodes():
    pass


def test_value_in_linked_list():
    linked_list = Linked_List()
    linked_list.insert("apple")
    linked_list.insert("banana")
    assert linked_list.includes("apple")


def test_value_not_in_linked_list():
    pass


def test_collection_values_in_linked_list():
    pass

