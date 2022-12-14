# A function to determine the scenic score for a given tree
def total_scenic_score(current_tree, up, down, left, right):
    
    def scenic_score_for_side(current_tree, side):
        scenic_score = 0
        for neighbour_tree in side:
            if neighbour_tree >= current_tree:
                scenic_score += 1
                break
            if neighbour_tree < current_tree:
                scenic_score += 1
        return(scenic_score)
    
    scenic_score_up = scenic_score_for_side(current_tree, up)
    scenic_score_down = scenic_score_for_side(current_tree, down)
    scenic_score_left = scenic_score_for_side(current_tree, left)
    scenic_score_right = scenic_score_for_side(current_tree, right)

    return(scenic_score_up*scenic_score_down*scenic_score_left*scenic_score_right)