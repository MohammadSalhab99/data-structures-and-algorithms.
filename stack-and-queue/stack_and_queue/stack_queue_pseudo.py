from stack_and_queue.stackAndQueue import Stack
class pseudoQueue():
    s1= Stack()
    s2= Stack()
    size= 0
    def __init__(self):
        self.rear= None
    def enqueue(self,value):
        """This method uses stack to enqueue a value

        Args:
            value (_type_): we use the value to push to the stack
        """
        self.s1.push(value)
        self.size+=1
        self.rear= self.s1.peek()
    def dequeue(self):
        """The dequeue method is used to dequeue a value from the seconed stack after we push all the nodes from the first stack 

        Returns:
            _type_: the first node in the seconed stack
        """
        while self.size>=0:
            self.s2.push(self.s1.pop())
            self.size -=1
        return self.s2.pop()
        
    
        
        
    