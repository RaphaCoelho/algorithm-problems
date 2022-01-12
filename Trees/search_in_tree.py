class Tree:
    def __init__(self, root):
        self.left = None
        self.right = None
        self.root = root
        # print function

tree = Tree(20)
tree.left = Tree(14)
tree.right = Tree(35)
tree.left.left = Tree(15)
tree.left.right = Tree(18)
tree.right.left = Tree(37)
tree.right.right = Tree(40)
tree.right.right.right = Tree(60)

#               20 
#              /  \
#             14   35
#            / \   / \
#           15 18 37 40
#
def search(tree,key):

    if tree is None or tree.root == key:
        return print('Valor encontrado!', tree.root)
    if tree.root < key:
        return search(tree.right,key)
    elif tree.root > key:
        return search(tree.left,key)

search(tree,18)