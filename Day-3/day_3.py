# Read the input data from the provided file or input source
with open('input.txt') as f:
    list_of_rucksacks_with_items = f.read().strip().split('\n')

score_puzzle_1 = 0
score_puzzle_2 = 0

# Create a string with priorities so we can use it to determine the priority score
priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Solve puzzle 1: 
for rucksack in list_of_rucksacks_with_items:
    
    # Find the number of items in bots compartment of each rucksack
    number_of_items_per_compartment = int(len(rucksack) / 2)

    # Return the item that is present in both compartments by comparing each item in each compartment, and add it to the total score
    double_item = set(rucksack[0:number_of_items_per_compartment]).intersection(set(rucksack[number_of_items_per_compartment:len(rucksack)])).pop()
    score_puzzle_1 += priorities.find(double_item)+1

# Divide the list of elves in groups of 3
groups_of_elves = [list_of_rucksacks_with_items[x:x+3] for x in range(0, len(list_of_rucksacks_with_items), 3)]

# Solve puzzle 2: Check which item is in all three rucksacks, which must be the badge, and add the equivalent priority score to the total score
for group in groups_of_elves:
    badge = set(group[0]).intersection(set(group[1]), set(group[2])).pop()
    score_puzzle_2 += priorities.find(badge)+1

print(score_puzzle_1, score_puzzle_2)