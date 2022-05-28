from trees import TNode,BinaryTree


def FizzBuzzTree(tree):
    newNode = TNode(None)
    tree1 = BinaryTree()
    tree1.root = newNode
    root = tree.root
    root1 = tree1.root
    def traverse(root,root1):
        
        
        if not(root.value %3 or root.value %5):
            root1.value = 'fizzbuzz'
        else:
            if not(root.value %3):
                root1.value = 'fizz'
            else:
                if not(root.value %5):
                    root1.value = 'buzz'
                else:
                    root1.value = str(root.value)
        if root.left:
            root1.left = TNode(root.left.value)
            traverse(root.left,root1.left)
        if root.right:
            root1.right = TNode(root.right.value)
            traverse(root.right,root1.right)
    traverse(root,root1)
    return tree1

if __name__ == "__main__":
    from trees import BinaryTree ,TNode
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
    print(FizzBuzzTree(tree).pre_order())
  
