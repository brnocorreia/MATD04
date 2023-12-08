import random
from binary_tree import BinarySearchTree

# values = random.sample(range(1,100), 42)
values = [50, 30, 40, 70, 60, 80, 65]

bst = BinarySearchTree()
for v in values:
    bst.insert(v)

bst.inorder_traversal()
print('-----------')
bst.remove(70)
bst.inorder_traversal()
