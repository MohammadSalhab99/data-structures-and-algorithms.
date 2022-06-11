from merge_sort.merge_sort import Mergesort
first_list=[8,4,23,42,16,15]
Reverse_sorted= [20,18,12,8,5,-2]
Few_uniques= [5,12,7,5,5,7]
Nearly_sorted= [2,3,5,7,13,11]

def test_one():
    Mergesort(first_list)
    actual = first_list
    expected = [4,8,15,16,23,42]
    assert actual ==expected

def test_Reverse_sorted():
    Mergesort(Reverse_sorted)
    actual = Reverse_sorted
    expected = [-2,5,8,12,18,20]
    assert actual ==expected

def test_Few_uniques():
    Mergesort(Few_uniques)
    actual = Few_uniques
    expected = [5,5,5,7,7,12]
    assert actual ==expected


def test_Nearly_sorted():
    Mergesort(Nearly_sorted)
    actual = Nearly_sorted
    expected =[2,3,5,7,11,13]
    assert actual ==expected