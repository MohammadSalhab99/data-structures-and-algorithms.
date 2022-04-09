from cmath import exp
from trees_data_stracture.trees import BinaryTree , Binary_search_tree,TNode

def test_pre_order():
   node1 = TNode(1)
   node2 = TNode(2)
   node3 = TNode(3)
   node4 = TNode(4)
   node1.left = node2
   node1.right = node3
   node3.right = node4
   tree = BinaryTree()
   tree.root = node1
   actual = tree.pre_order()
   expected =  [1, 2, 3, 4]
   assert actual == expected
   
def test_in_order():
   node1 = TNode(1)
   node2 = TNode(2)
   node3 = TNode(3)
   node4 = TNode(4)
   node1.left = node2
   node1.right = node3
   node3.right = node4
   tree = BinaryTree()
   tree.root = node1
   actual = tree.in_order()
   expected = [2, 1, 3, 4]
   assert actual == expected
   
def test_post_order():
   node1 = TNode(1)
   node2 = TNode(2)
   node3 = TNode(3)
   node4 = TNode(4)
   node1.left = node2
   node1.right = node3
   node3.right = node4
   tree = BinaryTree()
   tree.root = node1
   actual = tree.post_order()
   expected = [2, 4, 3, 1]
   assert actual == expected
   
def test_empty():
   tree = BinaryTree()
   actual = tree.post_order()
   expected = []
   assert actual == expected