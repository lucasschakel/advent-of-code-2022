from anytree import Node
import re

with open('input.txt') as f:
    input = f.read().strip().split('\n')

# Set the start of the tree.
root = Node("dir_/")
current_node = root
# Create a tree from the input, to get a better overview and define which files belong in which directories.
for line in input:
    # Move up in tree. Setting the current node to it's parent.
    if line.startswith("$ cd .."):
      current_node = current_node.parent  
    # A change of directory is found, meaning a new directory is found, so save it and create a node. Skip root node by skipping over '/'. 
    elif line.startswith("$ cd ") and '/' not in line:
      directory = ('dir_' + line.split(" ", 2)[2])
      current_node = Node(directory, parent=current_node)
    # If a file is found, create a node from it under the curent parent.
    elif line[0].isdigit():
        Node(line, parent=current_node)

# Function that sums all file sizes for a given directory.
def directory_size_finder(node):
    directory_size = 0
    # Iterate over the descendants and check if their name contains a number, which would indicate that it is a file.
    for node in list(node.descendants):
        if re.search(r"\d", node.name):
            directory_size += int(node.name.split(' ', 1)[0])
    return(directory_size)

puzzle_1_total_size = 0
puzzle_2_potential_directories_to_remove = []
size_to_free_up = 30000000 - (70000000 - directory_size_finder(root))

for node in root.descendants:
    if node.name.startswith('dir'):
        
        # Solve puzzle 1: for each directory, check if the total size is at moest 100000. If so, add it to the total size.
        if directory_size_finder(node) <= 100000:
            puzzle_1_total_size += directory_size_finder(node)
            
        # Solve puzzle 2: Find how much size we need to free up, find all directories that we could delete to create enough space, return the smallest of those directories. 
        if directory_size_finder(node) >= size_to_free_up:
            puzzle_2_potential_directories_to_remove.append(directory_size_finder(node))

print(puzzle_1_total_size)
print(min(puzzle_2_potential_directories_to_remove))