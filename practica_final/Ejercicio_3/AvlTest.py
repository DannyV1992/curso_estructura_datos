from AVLTree import AVLTree

Tree = AVLTree()       
root = None
root = Tree.insert_node(root,78)
root = Tree.insert_node(root,393)
root = Tree.insert_node(root,90)
root = Tree.insert_node(root,120)
root = Tree.insert_node(root,1)
root = Tree.insert_node(root,10)
root = Tree.insert_node(root,99)
root = Tree.insert_node(root,34)
root = Tree.insert_node(root,54)
root = Tree.insert_node(root,121)
root = Tree.insert_node(root,14)
root = Tree.insert_node(root,60)
root = Tree.insert_node(root,35)

print("PREORDER")
Tree.preOrder(root, "")
print("\n\nINORDER")
Tree.inOrder(root, "")
print("\n\nPOSTORDER")
Tree.postOrder(root, "")