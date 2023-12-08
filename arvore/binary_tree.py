from node import Node

class BinaryTree:
    def __init__(self, data = None, node=None):
        if node:
            self.root = node
        elif data:
            self.root = Node(data)
        else:
            self.root = None
    
    #Percurso em pós ordem
    def post_order_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.post_order_traversal(node.left)
        if node.right:
            self.post_order_traversal(node.right)
        print(node)
    
    #Percurso em ordem
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node:
            if node.left:
                self.inorder_traversal(node.left)
            print(node)
            if node.right:
                self.inorder_traversal(node.right)

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1    
        return hleft + 1

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        aux = self.root
        while aux:
            parent = aux
            if value < aux.data:
                aux = aux.left
            else:
                aux = aux.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        return self.__search(value, self.root)
    
    def remove(self, value, node=None):
        if node is None:
            node = self.root
        
        if node is None:
            return node
        
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            else:
                sub = self.__min(node.right)
                node.data = sub
                node.right = self.remove(sub, node.right)

        return node
    
    def __search(self, value, node):
        if node is None or node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self.__search(value, node.left)
        return self.__search(value, node.right)
    
    def __min(self, node=None):
        if node is None:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def __max(self, node=None):
        if node is None:
            node = self.root
        while node.right:
            node = node.right
        return node.data
