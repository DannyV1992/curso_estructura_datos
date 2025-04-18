from Avl_Node import avl_Node

class AVLTree(object):
         
    def insert_node(self, root, value):
 
        if not root:
            return avl_Node(value)
        elif value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)
 
        root.height = 1 + max(self.avl_Height(root.left),
                              self.avl_Height(root.right))
 
        # Update the balance factor and balance the tree
        balanceFactor = self.avl_BalanceFactor(root)
        if balanceFactor > 1:
            if value < root.left.value:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
 
        if balanceFactor < -1:
            if value > root.right.value:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
 
        return root
    def avl_Height(self, root):
        if not root:
            return 0
        return root.height
 
    # Get balance factore of the node
    def avl_BalanceFactor(self, root):
        if not root:
            return 0
        return self.avl_Height(root.left) - self.avl_Height(root.right)
     
    def avl_MinValue(self, root):
        if root is None or root.left is None:
            return root
        return self.avl_MinValue(root.left)
 
    def preOrder(self, root, pos):
        if not root:
            return
        print("{0}{1}".format(root.value,pos), end=" ")
        self.preOrder(root.left, "L")
        self.preOrder(root.right, "R")
         
    def inOrder(self, root, pos):
        if not root:
            return
        self.inOrder(root.left, "L")
        print("{0}{1}".format(root.value, pos), end=" ")
        self.inOrder(root.right, "R")

    def postOrder(self, root, pos):
        if not root:
            return
        self.postOrder(root.left,"L")
        self.postOrder(root.right, "R")        
        print("{0}{1}".format(root.value, pos), end=" ")

    def leftRotate(self, b):
        a = b.right
        T2 = a.left
        a.left = b
        b.right = T2
        b.height = 1 + max(self.avl_Height(b.left),
                           self.avl_Height(b.right))
        a.height = 1 + max(self.avl_Height(a.left),
                           self.avl_Height(a.right))
        return a
 
     
    def rightRotate(self, b):
        a = b.left
        T3 = a.right
        a.right = b
        b.left = T3
        b.height = 1 + max(self.avl_Height(b.left),
                           self.avl_Height(b.right))
        a.height = 1 + max(self.avl_Height(a.left),
                           self.avl_Height(a.right))
        return a
         
    def delete_node(self, root, value):
 
        # Find the node to be deleted and remove it
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.avl_MinValue(root.right)
            root.value = temp.key
            root.right = self.delete_node(root.right, temp.value)
        if root is None:
            return root
 
        # Update the balance factor of nodes
        root.height = 1 + max(self.avl_Height(root.left), self.avl_Height(root.right))
        balanceFactor = self.avl_BalanceFactor(root)
 
        # Balance the tree
        if balanceFactor > 1:
            if self.avl_BalanceFactor(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.avl_BalanceFactor(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root