from is_tree_visible import is_tree_visible
from total_scenic_score import total_scenic_score

with open('input.txt') as f:
    input = f.read().strip().split('\n')

# To solve puzzle 1, first get the number of trees on the outside ring, as all are visible. Count them towards the total number of visible trees
total_number_of_visible_trees = len(input[0])*2 + len(input)*2 - 4
# To solve puzzle 2, make sure to save the total scenic score
all_scenic_scores = []

# Make sure to iterate over the whole input file keep track of the X and Y index
for y, line_of_trees in enumerate(input):
    for x, tree in enumerate(line_of_trees):
        
        # Make sure to only check trees that are not on the outer circle of the grid
        if y == 0 or x == 0 or y == len(line_of_trees)-1 or x == len(input)-1:
            pass
        else:
            # Get the trees on the left and right of the current tree, starting from current tree
            trees_on_right = [i for i in line_of_trees[x+1:]]
            trees_on_left = list(reversed([i for i in line_of_trees[:x]]))
            
            # Get the trees above the current tree, starting from current tree
            trees_above = []
            for i in range(0, y):
                trees_above += input[i][x]
            trees_above = list(reversed(trees_above))

            # Get the trees below the current tree, starting from current tree
            trees_below = []
            for i in range(y+1, len(input)):
                trees_below += input[i][x]
            
            # Solve puzzle 1: check if tree is visible, if so, count it towards to total number of visible trees.
            visible = is_tree_visible(current_tree=tree, up=trees_above, down=trees_below, left=trees_on_left, right=trees_on_right)
            if visible:
                total_number_of_visible_trees += 1

            # Solve puzzle 2: get the scenic score for every tree and print the highest score later on.
            all_scenic_scores.append(total_scenic_score(current_tree=tree, up=trees_above, down=trees_below, left=trees_on_left, right=trees_on_right))

print(total_number_of_visible_trees)
print(max(all_scenic_scores))