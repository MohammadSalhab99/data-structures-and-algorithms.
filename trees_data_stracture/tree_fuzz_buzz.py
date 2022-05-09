from trees_data_stracture.trees import BinaryTree ,TNode

def FizzBuzzTree(tree):
    root = tree.root
    def traverse(current):
        if not(current.value %3 or current.value %5):
            current.value = 'fuzzbuzz'
        else:
            if not(current.value %3):
                current.value = 'fuzz'
            else:
                if not(current.value %5):
                    current.value = 'buzz'
                else:
                    current.value = str(current.value)
        if current.left:
            traverse(current.left)
        if current.right:
            traverse(current.right)
    traverse(root)
    return tree


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
FizzBuzzTree(tree)
print(tree.pre_order())