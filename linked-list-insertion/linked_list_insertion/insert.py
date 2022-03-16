class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
  
  def __init__(self):
    self.head = None
   
  def insert(self,value):
    try:
      node=Node(value)
      if self.head == None:
          self.head = node
          # print(self.head.value)
      else:
          node.next=self.head
          self.head=node
          # print(self.head.value)

          
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
                result += f'[{current.value}] -> '
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
      
  def insert_before(self,key,value):
    """
    insert a node before a node with a given key
    """
    new_node = Node(value)
    current = self.head
    while current != None:
          if current.value == value:
            node.next = current
            self.head = new_node
            break 
          if current.next != None:
            if current.next.value == key:
                new_node.next = current.next
                current.next = new_node
                print ("added")
                break
          current= current.next


  def insert_after(self,key,value):
    """
    insert a node after a node with a given key
    """
    new_node = Node(value)
    current = self.head
    while current != None:
      if current.value == key:
          new_node.next = current.next
          current.next = new_node
          break
      current= current.next



# link_list= Linked_list()
# link_list.insert( 1)
# link_list.insert( 3)
# link_list.insert( 2)
# link_list.insert_after(3,5)

# print(link_list.to_string())




    """
    append a node the end of the linked list
    """
     """
    check if the node the have the given value is exist in the list or not
    """
     """
    insert a node to the beginning of the linked list
    
    """