from AVLTree import *

bst1 = AVLTree()

bst1.insert(10)
bst1.insert(20)
bst1.insert(5)
bst1.insert(80)
bst1.insert(90)
bst1.insert(7550)
bst1.insert(30)
bst1.insert(77)
bst1.insert(15)
bst1.insert(40)

bst1.delete(7550)
bst1.delete(10)

bst1.preOrder(bst1.getRoot())
print()
bst1.inOrder(bst1.getRoot())
print()
bst1.postOrder(bst1.getRoot())