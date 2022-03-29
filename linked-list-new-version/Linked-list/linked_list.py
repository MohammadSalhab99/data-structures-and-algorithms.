class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
  
  def __init__(self):
    self.head = None
    self.size = 0
   
  def insert(self,value):
    """
    insert a node to the beginning of the linked list
    """
    try:
      node=Node(value)
      if self.head == None:
          self.head = node
          self.size += 1
          # print(self.head.value)
      else:
          node.next=self.head
          self.head=node
          self.size += 1
          # print(self.head.value)

          
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
    """
    This function returns a string representation of the linked list
    
    """
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
    

    """
    append a node the end of the linked list
    """

   
    try:
  
      node = Node(data)
      if self.head == None:
          self.head = node
          self.size += 1
      else:
          current = self.head
          while current.next != None:
              current = current.next
              self.size += 1
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
                self.size += 1
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
          self.size += 1
          break
      current= current.next
 
  def reverse(self):
    """
    This function reverse the order of the nodes in the linked list 
    """
    prev = None
    current = self.head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    self.head = prev
  def kthFromEnd(self, k):
    """
    this function returns the kth node from the end of the linked list
    """
    if(k==0 and self.size==1):
      return self.head.value

    if(k>=self.size):
      
      return ("out of range")
    
    self.reverse()
    
    k=abs(k) # handle negative 
    count = 0
    current = self.head
    while current.next != None :
      if k==count :
      
        return current.value 
      else :
       
        count+=1
        current=current.next




link_list= Linked_list()
link_list.insert( 2)
link_list.insert( 8)
link_list.insert( 3)
link_list.insert( 1)

# link_list.insert_after(3,5)
print(link_list.to_string())
print(link_list.kthFromEnd(2))
print(link_list.kthFromEnd(-2))


print(link_list.to_string())


