def print_tree_inorder(tree):
    if tree is None: return
    if tree.left is not None or tree.right is not None:
        print("(", end=" ")
    print_tree_inorder(tree.left)
    print(tree.cargo, end=" ")
    print_tree_inorder(tree.right)
    if tree.left is not None or tree.right is not None:
        print(")", end=" ")
