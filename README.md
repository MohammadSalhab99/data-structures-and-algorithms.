# Trees
A tree is a collection of entities called nodes. Nodes are connected by edges. Each node contains a value or data, and it may or may not have a child node .

## Challenge
    Features
    Node
    Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
    Binary Tree
    Create a Binary Tree class
    Define a method for each of the depth first traversals:
    pre order
    in order
    post order which returns an array of the values, ordered appropriately.
    Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
    Binary Search Tree
    Create a Binary Search Tree class
    This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
    Add
    Arguments: value
    Return: nothing
    Adds a new node with that value in the correct location in the binary search tree.
    Contains
    Argument: value
    Returns: boolean indicating whether or not the value is in the tree at least once.
## Approach & Efficiency
using recursive approuch to traverse the tree the comlixity is O(N)
## API
IN the description of the challenge 

# breadth_first_search
## Challenge Summary

    Write a function called breadth first
    Arguments: tree
    Return: list of all values in the tree, in the order they were encountered

## Whiteboard Process
![breadth-first-search](https://user-images.githubusercontent.com/61474974/163270599-946d994b-e1c9-453b-8e16-d4a32a779970.jpg)

https://miro.com/app/board/uXjVO8n0uew=/
## Approach & Efficiency
I used the recursive approuch to traverse through the the tree, it doesn't take a lot of time from me to find the solution, and the complexity of the algorithm is O(n) in the worst case 

## Solution
The solution in the python file and in the Whiteboard 


# Find_max Summary 

This challenge asks to write a method in tree class to get the maximum value of the tree
## Whiteboard Process
![tree-max (1)](https://user-images.githubusercontent.com/61474974/163578893-076da6ab-b938-40a3-8f8d-db67eee2206f.jpg)

## Approach & Efficiency
I used the recursive approuch to traverse through the tree and find the maximum value of the tree the time complexity is O(n) in the worst case and the space complexity is O(1)
## Solution
def get_max(self):
        if self.root == None:
            return "tree is empty"
        _max = self.root.value

        def _walk(node):
            nonlocal _max
            if node.value > _max:
                _max = node.value
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return _max



