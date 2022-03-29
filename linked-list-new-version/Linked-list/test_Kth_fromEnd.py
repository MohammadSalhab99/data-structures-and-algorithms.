from linked_list.linked_list import Linked_list



initial_list = Linked_list()
initial_list.insert(2)
initial_list.insert(3)
initial_list.insert(1)
initial_list.insert(5)
initial_list.insert(7)

one_element = Linked_list()
one_element.insert(3)



def test_middle_k():
    actual= initial_list.kthFromEnd(1)
    expected= 3
    assert actual== expected
def test_k_equalSize():
    actual=initial_list.kthFromEnd(5)
    expected="out of range"
    assert actual== expected

def test_k_greaterSize():
    actual=initial_list.kthFromEnd(7)
    expected="out of range"
    assert actual== expected
def test_k_negative():
    actual=initial_list.kthFromEnd(-1)
    expected=5
    assert actual== expected
def test_size_one():
    actual=one_element.kthFromEnd(0)
    expected=3
    assert actual== expected



    