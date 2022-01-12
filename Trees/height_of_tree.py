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

def get_height(tree):
    if tree is None:
        return 0
    else:
        left_branch = get_height(tree.left)
        right_branch = get_height(tree.right)   

        return max(left_branch, right_branch) + 1

print('altura: ', str(get_height(tree)))
