from quick_sort.quick_sort import QuickSort

def test_insertion_error():
    assert QuickSort([4, 8, 23, 16, 42, 15],0,5)==[4, 8, 15, 16, 23, 42]
def test_insertion_error1():
    assert QuickSort([20,18,12,8,5,-2],0,5)==[-2, 5, 8, 12, 18, 20]
def test_insertion_error2():
    assert QuickSort([5,12,7,5,5,7],0,5)==[5, 5, 5, 7, 7, 12]
def test_insertion_error3():
    assert QuickSort([2,3,5,7,13,11],0,5)==[2, 3, 5, 7, 11, 13]