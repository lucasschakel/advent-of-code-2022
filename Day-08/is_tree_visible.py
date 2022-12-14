# A function to check on each side of the tree is visible. If it is visible from one of the sides, return True.
def is_tree_visible(current_tree, up, down, left, right):  
    if all(tree < current_tree for tree in up):
        return(True)
    elif all(tree < current_tree for tree in down):
        return(True)
    elif all(tree < current_tree for tree in left):
        return(True)
    elif all(tree < current_tree for tree in right):
        return(True)
    else:
        return(False)