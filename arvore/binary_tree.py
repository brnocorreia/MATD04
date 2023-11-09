from node import Node

class BinaryTree:
    def __init__(self, data = None, node=None):
        if node:
            self.root = node
        elif data:
            self.root = Node(data)
        else:
            self.root = None
    
    #Percurso em ordem simétrica
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')

    #Percurso em pós ordem
    def post_order_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.post_order_traversal(node.left)
        if node.right:
            self.post_order_traversal(node.right)
        print(node)
    
    #Percurso em ordem simétrica
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
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
    
    def __search(self, value, node):
        if node is None or node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            self.__search(value, node.left)
        return self.__search(value, node.right)


if __name__ == "__main__":
    # root = Node(7)
    # tree = BinaryTree(root)

    # tree.root.left = Node(18)
    # tree.root.right = Node(14)

    # print(tree.root)
    # print(tree.root.right)
    # print(tree.root.left)

    # tree = BinaryTree()
    # n1 = Node('I')
    # n2 = Node('N')
    # n3 = Node('S')
    # n4 = Node('C')
    # n5 = Node('R')
    # n6 = Node('E')
    # n7 = Node('V')
    # n8 = Node('A')
    # n9 = Node('5')
    # n0 = Node('3')

    # n6.left = n7
    # n6.right = n8
    # n5.left = n6
    # n5.right = n9
    # n3.left = n4
    # n3.right = n5
    # n2.left = n1
    # n2.right = n3
    
    # tree.root = n2

    tree = BinaryTree()
    n1 = Node('I')
    n2 = Node('N')
    n3 = Node('S')
    n4 = Node('C')
    n5 = Node('R')
    n6 = Node('E')
    n7 = Node('V')
    n8 = Node('A')
    n9 = Node('5')
    n0 = Node('3')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0

    tree.post_order_traversal()
    print(f'A altura da árvore é {tree.height()}')