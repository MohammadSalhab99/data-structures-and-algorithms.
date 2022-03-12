class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
  
  def __init__(self,value):
    self.head = None
    
  def insert(self,value):
    try:
      node=Node(value)
      if self.head == None:
          self.head = node
      else:
          node.next=self.head
          self.head=node
    except:
      print("Error in insert method")
    
  def includes (self,value):
    try:
      current=self.head
      while current and current.next != None:
          if current.value == value:
              return True
          current=current.next
      return False
    except:
      print("Error in includes method")
  def to_string(self):
    try:
        current=self.head
        result=''

        if current == None:
            return 'Empty List'
        else:
            while current:
                result += f'{{{current.value}}}->'
                current=current.next   
            result += f'NULL'
        return result 
    except: 
      print("Error in to_string method")

    
    def append(self, data):
    try:
    
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    except:
        print("append Error")