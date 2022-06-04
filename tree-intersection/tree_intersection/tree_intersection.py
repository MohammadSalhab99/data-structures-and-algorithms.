from tree_intersection.hashtable import HashTable

def two_trees_intersection(tree1, tree2):
  
    htable = HashTable()
    list =[]
    list1 = []
    def traverse(root1,root2):
        list.append(root1.value)
        htable.__setitem__(str(root1.value),str(root2.value))
        if root1.left and root2.left:
           traverse(root1.left,root2.left)
        if root1.right and root2.right:
           traverse(root1.right,root2.right)
    traverse(tree1.root,tree2.root)
    for i in list:
        idx = htable._get_hash(str(i))
        if htable.map[idx][0][0] == htable.map[idx][0][1]:
            list1.append(i)
    

    return list1


