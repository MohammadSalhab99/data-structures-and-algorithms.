from stack_and_queue.stack_queue_pseudo import pseudoQueue
import pytest


def test_enqueue():
    queue =pseudoQueue()
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(7)
    actual = queue.rear
    expected = 7
    assert actual == expected
    
def test_enqueue():
    queue =pseudoQueue()
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(7)
    actual = queue.dequeue()
    expected = 3
    assert actual == expected
    