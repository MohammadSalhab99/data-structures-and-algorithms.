from stack_and_queue.stackAndQueue import Stack,Queue
import pytest


def test_push(stack):


  actual = stack.top.value
  expected = 2
  assert actual == expected
  
def test_pop(stack):
 

  actual= stack.pop()
  expected =2
  assert actual == expected


def test_peek_of_stack(stack):
  

  actual = stack.peek()
  expected = 2
  assert actual == expected


def test_is_empty_stack():
  stack=Stack()
  actual = stack.is_empty()
  expected = True
  assert actual == expected
  

 #decorator
@pytest.fixture
def stack():
 
  stack = Stack()
  stack.push(5)
  stack.push(3)
  stack.push(2)

  return stack

def test_enqueue():
  queue=Queue()
  queue.enqueue("zaid")
  queue.enqueue("raneem")
  queue.enqueue("raghad")

  actual = queue.rear.value
  expected = "raghad"

  #  actual = queue.front.value
  # expected = "zaid"
  
  assert actual == expected
  
def test_dequeue():
  queue=Queue()
  queue.enqueue("zaid")
  queue.enqueue("raneem")
  queue.enqueue("raghad")
  queue.dequeue()
  acutal =queue.front.value
  
  expected = "raneem"
  assert acutal == expected
  
  
def test_isEmpty():
  queue=Queue()
  actual= queue.is_empty()
  expected = True
  assert actual == expected
  
def test_peek_of_queue():
  queue=Queue()
  queue.enqueue("zaid")
  queue.enqueue("raneem")
  queue.enqueue("raghad")
  actual = queue.peek()
  expected = "zaid"
  assert actual == expected


  
    
  

  
  