def check_bst_util(root, min_value, max_value):
    if root is None:
        return True
    if not (min_value < root.value < max_value):
        return False
    return check_bst_util(root.left, min, root.value) and check_bst_util(root.right, root.value, max)


def check_bst(root):
    return check_bst_util(root, - maxsize, maxsize)