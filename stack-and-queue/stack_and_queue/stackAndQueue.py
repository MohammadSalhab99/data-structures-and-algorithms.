class Node :
  def __init__(self,value):
    self.value=value
    self.next=None 

class Stack :
  def __init__(self,node=None):
    self.top = node 

  def push(self,value):
    node = Node(value)
    node.next = self.top
    self.top = node 

  def pop(self) :
    temp = self.top
    self.top = self.top.next
    temp.next= None

    return temp.value

  def peek(self):
    if self.is_empty():
        raise ValueError("Empty")
    return self.top.value
   
  def is_empty(self):
    """method to check if stack is impty
     return boolean
    """
    return self.top == None 
     # return self.top



class Queue :
  def __init__(self):
    self.front=None
    self.rear=None

  def enqueue(self,value):
    node = Node(value)

    if not self.front :
      self.rear = node 
      self.front = node 
      
    else:  
      self.rear.next = node 
      self.rear = node 
      
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