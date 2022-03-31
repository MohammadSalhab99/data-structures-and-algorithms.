# Stacks and Queues

## Challenge
Create the following methods for the queue class:
dequeue
    Arguments: none
    Returns: the value from node from the front of the queue
    Removes the node from the front of the queue
    Should raise exception when called on empty queue
    peek
    Arguments: none
    Returns: Value of the node located at the front of the queue
    Should raise exception when called on empty stack
    is empty
    Arguments: none
    Returns: Boolean indicating whether or not the queue is empty
## Approach & Efficiency
The big O of all the methods is O(1)

## API
### Stack
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
    The class should contain the following methods:
    push
    Arguments: value
    adds a new node with that value to the top of the stack with an O(1) Time performance.
    pop
    Arguments: none
    Returns: the value from node from the top of the stack
    Removes the node from the top of the stack
    Should raise exception when called on empty stack
    peek
    Arguments: none
    Returns: Value of the node located at the top of the stack
    Should raise exception when called on empty stack
    is empty
    Arguments: none
    Returns: Boolean indicating whether or not the stack is empty.
### Queue
Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
The class should contain the following methods:
    enqueue
    Arguments: value
    adds a new node with that value to the back of the queue with an O(1) Time performance.
    dequeue
    Arguments: none
    Returns: the value from node from the front of the queue
    Removes the node from the front of the queue
    Should raise exception when called on empty queue
    peek
    Arguments: none
    Returns: Value of the node located at the front of the queue
    Should raise exception when called on empty stack
    is empty
    Arguments: none
    Returns: Boolean indicating whether or not the queue is empty

## pseudo Queue
### Challenge Summary
Create a new class called pseudo queue.
Do not use an existing Queue.
Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
Internally, utilize 2 Stack instances to create and manage the queue
Methods:
enqueue
Arguments: value
Inserts value into the PseudoQueue, using a first-in, first-out approach.
dequeue
Arguments: none
Extracts a value from the PseudoQueue, using a first-in, first-out approach.h

#### Whiteboard Process
![stack-queue-pseudo](https://user-images.githubusercontent.com/61474974/160931645-31d7d256-c443-4cf2-8635-415f967149be.jpg)


#### Approach & Efficiency
The Big O of the  methods is O(n) where n is the number of nodes 

#### Solution
In python files
