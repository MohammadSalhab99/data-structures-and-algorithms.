
class dog ():
    def __init__(self):
        self.value = "dog"
        self.next = None

class cat ():
    def __init__(self):
        self.value = "cat"
        self.next = None
        
class AnimalShelter ():
    def __init__(self):
        """intiat front and the rear of the queue"""

        self.front=None
        self.rear=None
        
    def enqueue(self,animal):
        if animal=="dog":
            node = dog()

            if not self.front :
                self.rear = node 
                self.front = node
            else:  
                self.rear.next = node 
                self.rear = node 
        if animal=="cat":
            node = cat()

            if not self.front :
                self.rear = node 
                self.front = node 
            else:  
                self.rear.next = node 
                self.rear = node 
                
    def dequeue(self,pref):
        while self.next !=None:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            
            return temp.value
       # to bo continue