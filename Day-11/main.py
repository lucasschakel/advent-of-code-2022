import re

with open('input.txt') as f:
    input = f.read().strip().split('\n')

# Function to complete the whole proces a monkey goes through with each item.
def operation(worry_level, index, input):
    old = int(worry_level)
    new = int(eval(input[index+2].split('=')[1].strip()) / 3)
    monkey_to_throw_to = monkey_test(new, divider, receiving_monkey_true, receiving_monkey_false)
    return(new, monkey_to_throw_to)

# Function to decide to which monkey an item is thrown. If worry level can be devided by the devider, the item gets thrown to the true-monkey. If not, it gets thrown to the false-monkey.
def monkey_test(worry_level, divider, receiving_monkey_true, receiving_monkey_false):
    if worry_level % int(divider) == 0:
        return(receiving_monkey_true)
    return(receiving_monkey_false)
    
# First iterate over all monkeys and check which items they have and create a dict to keep track of number of times a monkey checked an item.
monkeys_and_items = {}
monkeys_and_score = {}
for index, line in enumerate(input):
    if 'Monkey' in line:
        monkey_number = int(line[-2:-1])
        monkeys_and_items[monkey_number] = re.findall(r"\d+", input[index+1])
        monkeys_and_score[monkey_number] = 0

# In a round...
for _ in range(20):
    # For each monkey...
    for index, line in enumerate(input):
        if 'Monkey' in line:
            # Get all the needed variables for the monkey
            current_monkey = int(line[-2:-1])
            worry_levels_of_items_on_monkey = re.findall(r"\d+", input[index+1])
            divider = int(input[index+3].split()[-1])
            receiving_monkey_true = int(input[index+4].split()[-1])
            receiving_monkey_false = int(input[index+5].split()[-1])
            
            # Make sure their worry levels are iterable.
            worry_levels = []
            for worry_level in monkeys_and_items[current_monkey]:
                worry_levels.append(worry_level)
            
            # For each worry level...
            for worry_level in worry_levels:
                # Count that a monkey inspected an item
                monkeys_and_score[current_monkey] += 1
                
                # Do the operation an inspection goes through
                result_from_inspection = operation(worry_level, index, input)
                new_worry_level = result_from_inspection[0]
                monkey_to_throw_to = result_from_inspection[1]

                # Throw the item from monkey to monkey
                monkeys_and_items[monkey_to_throw_to].append(new_worry_level)
                monkeys_and_items[current_monkey].pop(0)

# Calculate score of puzzle 1
scores_sorted = sorted(monkeys_and_score.values(), reverse=True)
total_score = scores_sorted[0] * scores_sorted[1]
print(total_score)