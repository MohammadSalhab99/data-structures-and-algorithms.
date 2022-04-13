from trees_data_stracture.trees import *
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

def test_breadth_first():
    actual = tree_breadth_first(tree)
    expected = [2,3,1,4,7,25,11]
    assert actual == expected
tree2 = BinaryTree()
def test_breadth_first_is_emtpy():
    actual = tree_breadth_first(tree2)
    expected = "empty tree"
    assert actual == expected