from linked_list.linked_list import Linked_list




initial_list = Linked_list()
initial_list.insert(2)
initial_list.insert(3)
initial_list.insert(1)

def test_add_to_end():
    initial_list.append(5)
    actual = initial_list.to_string()
    expected = "[1] -> [3] -> [2] -> [5] -> NULL"
    assert actual == expected

def test_add_n_to_end():
    list_of_values= [4,6,9]
    for i in list_of_values:
        initial_list.append(i)
    actual = initial_list.to_string()
    expected = "[1] -> [3] -> [2] -> [5] -> [4] -> [6] -> [9] -> NULL"
    assert actual == expected

def test_insert_before():
    initial_list.insert_before(5,0)
    actual = initial_list.to_string()
    expected = "[1] -> [3] -> [2] -> [0] -> [5] -> [4] -> [6] -> [9] -> NULL"
    assert actual == expected

def test_insert():
    initial_list.insert(10)
    actual = initial_list.to_string()
    expected = "[10] -> [1] -> [3] -> [2] -> [0] -> [5] -> [4] -> [6] -> [9] -> NULL"
    assert actual == expected

def test_insert_after():
    initial_list.insert_after(0,30)
    actual = initial_list.to_string()
    expected = "[10] -> [1] -> [3] -> [2] -> [0] -> [30] -> [5] -> [4] -> [6] -> [9] -> NULL"
    assert actual == expected