class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
  
  def __init__(self):
    self.head = None
    
  def insert(self,value):
    """
    insert a node to the beginning of the linked list
    
    """
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
    """
    check if the node the have the given value is exist in the list or not
    """
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
    """
    append a node the end of the linked list
    """
    # try:
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

   
  
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
            if current.next != None
              if current.next.value == key:
                  new_node.next = current.next
                  current.next = new_node
                  break


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
         



# node1= Node(1)
# node2= Node(3)
# node3= Node(2)

# link_list= Linked_list()
# link_list.insert( node1)
# link_list.insert( node2)
# link_list.insert( node3)
# link_list.print()

