import re

with open('input.txt') as f:
    list_of_section_assignment_pairs = f.read().strip().split('\n')

score_puzzle_1 = 0
score_puzzle_2 = 0

for section_pair in list_of_section_assignment_pairs:
    
    section_1 = []
    section_2 = []

    # Strip relevant numbers from each section pair
    numbers_in_section_pair = re.findall(r'\d+', section_pair)

    # Check how many sections each elf in each pair has
    section_size_1 = int(numbers_in_section_pair[1]) - int(numbers_in_section_pair[0]) + 1
    section_size_2 = int(numbers_in_section_pair[3]) - int(numbers_in_section_pair[2]) + 1
    
    # Create a list of sections for each elf, starting from the correct number
    for ID_number in range(section_size_1):
        section_1.append(int(numbers_in_section_pair[0]) + ID_number)
    for ID_number in range(section_size_2):
        section_2.append(int(numbers_in_section_pair[2]) + ID_number)
    
    # Solve puzzle 1: If the number of numbers that are in both sections is equal to the total length of either of the sections, it means that one of the sections fully overlaps, so we can add it to the score.
    if len(set(section_1).intersection(set(section_2))) == len(section_2) or len(set(section_1).intersection(set(section_2))) ==len(section_1):
        score_puzzle_1 += 1

    # Solve puzzle 2: If the number of numbers that are in both sections is more than 0, it means there is at least one IC_number that overlaps, so we can count that assignment pair towards the score.
    if len(set(section_1).intersection(set(section_2))) > 0:
        score_puzzle_2 += 1

print(score_puzzle_1, score_puzzle_2)