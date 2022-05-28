from trees_data_stracture.tree_fizz_buzz import FizzBuzzTree
from trees_data_stracture.trees import TNode,BinaryTree
node1 = TNode(15)
node2 = TNode(3)
node3 = TNode(5)
node4 = TNode(4)
node5 = TNode(7)
node6 = TNode(25)
node7 = TNode(10)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

tree = BinaryTree()
tree.root = node1


def test_new_tree():
    actual =FizzBuzzTree(tree).pre_order()
    expected = ['fizzbuzz', 'fizz', '4', '7', 'buzz', 'buzz', 'buzz']
    assert actual ==expected

def test_old_tree():
    actual =tree.pre_order()
    expected = [15, 3, 4, 7, 5, 25, 10]
    assert actual ==expected