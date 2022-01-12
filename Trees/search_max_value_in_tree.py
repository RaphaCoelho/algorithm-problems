class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
tree = Tree(20)
tree.left = Tree(14)
tree.right = Tree(35)
tree.left.left = Tree(15)
tree.left.right = Tree(18)
tree.right.left = Tree(371)
tree.right.right = Tree(40)
tree.right.right.right = Tree(60)
tree.right.right.left = Tree(90)
tree.right.left.right = Tree(65)
tree.right.left.left = Tree(12)
tree.left.left.left = Tree(80)
tree.left.left.right = Tree(72)
tree.left.right.left = Tree(218)
tree.left.right.right = Tree(382)

#                     20 
#               /           \
#              14            35
#            /    \        /   \
#           15    18     371    40
#          / \   /   \   / \   / \
#         80 72 218 382 12 65 90 60
 
def findMax(tree):

    if (tree == None):
        return float('-inf')


    root = tree.data
    left_branch = findMax(tree.left)
    rigt_branch = findMax(tree.right)
    print('root:', root)
    print('esquerda:',left_branch)
    print('direita:',rigt_branch)
    print('-'*20)
    if (left_branch > root):
        root = left_branch
    if (rigt_branch > root):
        root = rigt_branch
    return root
 
 
# Function call
print("Maior valor: ",
        findMax(tree))