import pytest
from hashtable.hashtable import HashTable


@pytest.fixture
def hashtable():

    hashtable = HashTable()
    return hashtable


def test_hashtable_contains_bare_value(hashtable):

    hashtable.__setitem__("name", "Mohammad")
    assert hashtable.contains("name")


def test_hashable_contains_pair_in_a_linked_list(hashtable):

    hashtable.__setitem__("name", "Mohammad")
    hashtable.__setitem__("name", "Rami")
    assert hashtable.contains("name")


def test_hashtable_add(hashtable):

    hashtable.__setitem__("name", "Sami")
    assert hashtable.contains("name")


def test_hashable_add_same_key(hashtable):

    hashtable.__setitem__("khaled", "khaled")
    hashtable.__setitem__("khaled", "khaled")
    assert hashtable.contains("khaled")



def test_hashtable_get_returns_value(hashtable):

    expected = "Mohammad"
    hashtable.__setitem__("name", "Mohammad")
    assert hashtable.__getitem__("name") == expected


def test_hashtable_get_returns_correct_first_value(hashtable):

    expected = "Mohammad"
    hashtable.__setitem__("name", "Mohammad")
    hashtable.__setitem__("name", "Fayez")
    assert hashtable.__getitem__("name") == expected


def test_hashtable_get_returns_none_if_key_does_not_exist(hashtable):

    assert not hashtable.__getitem__("name")


def test_hashtable_contains_returns_false_if_key_does_not_exist(hashtable):

    assert not hashtable.contains("name")


def test_hashtable_handles_collisions(hashtable):
    expected = "grey"
    hashtable.__setitem__("coolr", "red")
    hashtable.__setitem__("cloor", "blue")
    hashtable.__setitem__("color", "grey")
    assert hashtable.__getitem__("color") == expected