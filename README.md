# Challenge Summary
        Write a function called zip lists
        Arguments: 2 linked lists
        Return: New Linked List, zipped as noted below
        Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
        Try and keep additional space down to O(1)
        You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
  

## Whiteboard Process
![zip_lists](https://user-images.githubusercontent.com/61474974/159483732-1a9bea83-578d-4e7a-acef-233e5e32f314.jpg)


## Approach & Efficiency
I used the same nodes to solve this problem to keep additional space down to O(1) 
I used the reverse method to reverse the linked list to find the kth node in from the end of the list , the I created the kth from the end of the list method, in this method I checked all the edge cases and found the kth node from the end of the list. The big O for these two methods is O(2n) -> O(n) 


## Solution
The solution in the Whiteboard and in the linked_list.py file 

## PR link
https://github.com/MohammadSalhab99/data-structures-and-algorithms./compare/linked-list?expand=1
