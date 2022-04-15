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

def test_get_max():
    actual = tree.get_max()
    expected = 25
    assert actual == expected
tree1 = BinaryTree()
def test_is_empty():
    acutal = tree1.get_max()
    expected = "tree is empty"
    assert acutal == expected