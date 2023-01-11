import pytest
from data_structures.binary_tree import BinaryTree, Node



def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

def test_max_val_positive():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(15)
    tree.root.right = Node(2)
    actual = tree.find_maximum_value()
    expected = 15
    assert actual == expected

def test_max_val_negative():
    tree = BinaryTree()
    tree.root = Node(-5)
    tree.root.left = Node(-15)
    tree.root.right = Node(-2)
    actual = tree.find_maximum_value()
    expected = -2
    assert actual == expected
