from tree_intersection.tree_intersection import two_trees_intersection
from tree_intersection.bt import BinaryTree, TNode


node1 = TNode(133)
node2 = TNode(2)
node3 = TNode(3)
node4 = TNode(4)
node1.left = node2
node1.right = node3
node3.right = node4
node5 = TNode(133)
node6 = TNode(6)
node7 = TNode(2)
node8 = TNode(4)
node5.left = node6
node5.right = node7
node7.right = node8
tree = BinaryTree()
tree.root = node1

tree2 = BinaryTree()
tree2.root =node5

def test_one():
    acutal = two_trees_intersection(tree,tree2)
    excepted = [133,4]
    assert acutal == excepted