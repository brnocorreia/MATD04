import random
from binary_tree import BinarySearchTree

values = random.sample(range(1,100), 42)

bst = BinarySearchTree()
for v in values:
    bst.insert(v)

bst.inorder_traversal()
