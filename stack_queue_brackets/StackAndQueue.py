class Node :
  """
  This class for creating nodes
  """
  def __init__(self,value):
    self.value=value
    self.next=None

class Stack :
  """
  Stack class for creating stack 
  """
  def __init__(self,node=None):
    self.top = node
    self.size = 0 
 

  def push(self,value):
    """
    This methods takes a value and push a node at the top of the stack that holds the given value

    """
    node = Node(value)
    node.next = self.top
    self.top = node 
    self.size+=1

  def pop(self) :
    """
    This method pop the value at the top of the stack and returns that value
    """
    temp = self.top
    self.top = self.top.next
    temp.next= None

    return temp.value

  def peek(self):
    """This method returns the value of the top value of the stack

    Raises:
        ValueError: if the stack is empty

    Returns:
        value: top value of the stack
    """
    if self.is_empty():
        raise ValueError("Empty")
    return self.top.value
   
  def is_empty(self):
    """
    method to check if stack is empty
    return boolean
    """
    return self.top == None 
     # return self.top



class Queue :
  def __init__(self):
    """intiat front and the rear of the queue"""

    self.front=None
    self.rear=None
    self.size = 0

  def enqueue(self,value):
    """This method takes a value and put it at the rear of the queue
    if the queue is empty the new node will in the front and the rear of the queue

    args: value
    """
    node = Node(value)

    if not self.front :
      self.rear = node 
      self.front = node 
      self.size+=1
      
    else:  
      self.rear.next = node 
      self.rear = node 
      self.size+=1
      
      
  def dequeue(self) :
    """
    this function is called dequeue that delete the first node in the queue
    """
    temp = self.front
    self.front = self.front.next
    temp.next = None
    
    return temp.value

  def is_empty(self):
    """this function returns whether the queue is empty or not

    Returns:
        Boolean: queue is empty or not empty
    """
    return self.front==None

  def peek(self):
    """this method returns the front value of the queue

    Raises:
        ValueError: Empty

    Returns:
        value: front value
    """
    if self.is_empty():
        raise ValueError("Empty")
    peek = self.front
    return peek.value
  
 