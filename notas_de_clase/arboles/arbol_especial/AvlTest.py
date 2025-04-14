from AVLTree import AVLTree

Tree = AVLTree()       
root = None
root = Tree.insert_node(root,40)
root = Tree.insert_node(root,60)
root = Tree.insert_node(root,50)
root = Tree.insert_node(root,70)
root = Tree.insert_node(root,71)
root = Tree.insert_node(root,61)
 
print("PREORDER\n")
Tree.preOrder(root, "")
print("\nINORDER")
Tree.inOrder(root, "")
print("\nPOSTORDER")
Tree.postOrder(root, "")