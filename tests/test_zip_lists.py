from linked_list.linked_list import Linked_list

list1 = Linked_list()

list1.insert(2)
list1.insert(3)
list1.insert(1)
list2 = Linked_list()
list2.insert(4)
list2.insert(9)
list2.insert(5)

def test_zip_the_same_length():
    actual = Linked_list.zip_lists(list1, list2).to_string()
    expected ="[1] -> [5] -> [3] -> [9] -> [2] -> [4] -> NULL"
    assert actual == expected
    # list1.insert(7)
list3 = Linked_list()

list3.insert(3)
list3.insert(1)
list4 = Linked_list()
list4.insert(4)
list4.insert(9)
list4.insert(5)
def test_zip_the_diffrent_length():
    actual =  Linked_list.zip_lists(list3, list4).to_string()
    expected ="[1] -> [5] -> [3] -> [9] -> [4] -> NULL"
    assert actual == expected

list5 = Linked_list()
list5.insert(2)
list5.insert(3)
list5.insert(1)
list6 = Linked_list()
list6.insert(9)
list6.insert(5)
def test_zip_the_diffrent2_length():
    actual =  Linked_list.zip_lists(list5, list6).to_string()
    expected ="[1] -> [5] -> [3] -> [9] -> [2] -> NULL"
    assert actual == expected
