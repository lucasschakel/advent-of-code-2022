import re

# Get the relevant steps from the moves so you can iterate over them
moves_without_text = []
with open('moves.txt') as f:
    moves = f.read().strip().split('\n')
for line in moves:
    moves_without_text.append(re.findall(r'\d+', line))

# Load crates as sublists in a list for each puzzle
with open('crates.txt') as f:
    crates_solution_1 = [x.rstrip('\n').split(" ") for x in f.readlines()]
with open('crates.txt') as f:
    crates_solution_2 = [x.rstrip('\n').split(" ") for x in f.readlines()]

for move in moves_without_text:
    # Define what every number in each move means for readability
    number_of_crates = int(move[0])
    from_position = int(move[1])-1    
    to_position = int(move[2])-1

    # Solve puzzle 1: Start loading of crates and putting them on other stacks by popping them of the from-stack and appending them to the to-stack. Repeat for the amount of crates needed.
    for i in range(0, number_of_crates):
        crates_solution_1[to_position].extend(crates_solution_1[from_position].pop())

    # Solve puzzle 2: Store the crates you need temporarily to keep the order, delete the creates from the stack you took them from, finally extend them to the new stack.
    temp_crates = crates_solution_2[from_position][-number_of_crates:]
    del crates_solution_2[from_position][-number_of_crates:]
    crates_solution_2[to_position].extend(temp_crates)

# Print solutions
for crate_stack in crates_solution_1:
    print(crate_stack[-1])
print('----')
for crate_stack in crates_solution_2:
    print(crate_stack[-1])