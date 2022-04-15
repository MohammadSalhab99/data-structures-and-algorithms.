

class Node:
    def __init__(self, value):
        self.value = value  ## TNode
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """
    push will add a new Node to the stack

    input: value
    output: None
    
    """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
    input: none
    doing: pop the top node from the stack 
    output: popped node's value
    """

        if self.is_empty():
            raise Exception("Stack is empty !")

        temp = self.top
        self.top = self.top.next
        temp.next = None

        return temp.value

    def is_empty(self):
        """
    input: None
    doing: Check if the top is none or not
    output: return a boolean
    """
        if self.top is None:
            return True
        return False


class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """
    Input: None
    doing: traverse a tree
    output: print values of the nodes of the tree in pre order (root->left->right)
    """
        
        arr=[]
        if self.root == None:
            return arr
        def _walk(node):
            arr.append(node.value)
            print(node.value)

            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return arr

    def pre_order_itiration(self):
        """
    A method to traverse the tree elements
    input: nothing
    output: print the value of each node
    """
        stack = Stack()
        current = self.root

        stack.push(current)

        while not stack.is_empty():
            current = stack.pop()
            print(current.value)

            if current.right:
                stack.push(current.right)

            if current.left:
                stack.push(current.left)
                
                
                
    def in_order(self):
        """
    Input: None
    doing: traverse a tree
    output: print values of the nodes of the tree in in order (left >> root >> right)
    """
        arr= []
        if self.root == None:
            return arr
        def _walk(node):
                if not node.left and not node.right:
                    arr.append(node.value)
                    print(node.value)
                    
                else:
                    if node.left:
                        _walk(node.left)
                    arr.append(node.value)
                    print(node.value)  
                    if node.right:
                        _walk(node.right)
        _walk(self.root)
        return arr
    
    # def in_order_itiration(self):
    #     """
    # A method to traverse the tree elements
    # input: nothing
    # output: print the value of each node
    # """
    #     stack = Stack()
    #     current = self.root

    #     stack.push(current)

    #     while not stack.is_empty():
            
    #         current = stack.pop()
    #         if current.right:
    #             stack.push(current.right)
    #         print(current.value)
                
    #         if current.left:
    #             stack.push(current.left)
    #         stack.push(current)
         
            
    def post_order(self):
        """
    Input: None
    doing: traverse a tree
    output: print values of the nodes of the tree in post order (left >> right >> root)
    """
        arr = []
        if self.root == None:
            return arr
        def _walk(node):
                if not node.left and not node.right:
                    #print(node.value)
                    arr.append(node.value)
                else:
                    if node.left:
                        _walk(node.left)
                    if node.right:
                        _walk(node.right)
                    arr.append(node.value)
                    print(node.value) 
        _walk(self.root)
        return arr
    def post_order_itiration(self):
        """
    A method to traverse the tree elements
    input: nothing
    output: print the value of each node
    """
        stack = Stack()
        current = self.root
        
        stack.push(current)

        while not stack.is_empty():
            if current.right:
                stack.push(current.right)
          
            if current.left:
                stack.push(current.left)
            current = stack.pop()
            print(current.value)
    def get_max(self):
        """This function taks a tree and returns the maximum value of that tree 

        Returns:
            value: the maximum value of the tree
        """
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
    

class Binary_search_tree(BinaryTree):
    """This class build a binary search tree

    Args:
        BinaryTree class: The class  Binary_search_tree inhirit from the binary tree class
    """
    def __init__(self):
       self.root = None
    def Add(self,value):
        """This method add to the tree depending on the value

        Args:
            value : the value to be added into the tree
        """
        node = TNode(value)
        def _walk(root):
            current = root
            
            if node.value > current.value:
                if current.right:
                    _walk(current.right)
                else:
                    current.right = node
            else:
                if node.value < current.value:
                    if current.left:
                        _walk(current.left)
                    else:
                        current.left = node 
        _walk(self.root)

        
    def contains(self,value):
        """This method returns True if the value is contained in the tree else return false

        Args:
            value : The value to be checked

        Returns:
            Boolean: wether the value is contained in the tree or not
        """
        # check = False
        node = TNode(value)
        def _walk(root):
            current = root
            if current.value==node.value:
                return True
            
            if current.left:
                _walk(current.left)
            if current.right:
                _walk(current.right)
            return False
                # if node.value > current.value:
                #     if current.right:
                #         _walk(current.right)
                #     else:
                #         current.right = node
                # elif node.value < current.value:
                #     if current.left:
                #         _walk(current.left)
                #     else:
                #         current.left = node
                # else:
                #     return False
        
        return _walk(self.root)
    
        
 








def tree_breadth_first(tree):
    if tree.root is None:
        return "empty tree"
    list1 = []
    list1.append(tree.root.value)
    def _walk(root):
        
        if root.left:
            list1.append(root.left.value)
        if root.right:
            list1.append(root.right.value)
    
        if root.left:
            _walk(root.left)
        if root.right:
            _walk(root.right)
    _walk(tree.root)
    return list1

if __name__ == '__main__':
    node1 = TNode(2)
    node2 = TNode(3)
    node3 = TNode(1)
    node4 = TNode(4)
    node5 = TNode(7)
    node6 = TNode(25)
    node7 = TNode(11)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    tree = BinaryTree()
    tree.root = node1
    bst= Binary_search_tree()
    tree.root = node1
    # bst.Add(5)
    # bst.pre_order_itiration()
    # print(bst.contains(4))
    print(tree_breadth_first(tree))

