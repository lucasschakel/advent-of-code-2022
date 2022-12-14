data = open('data.txt', 'r').read().split('\n')
score = 0

# A Y
# B X
# C Z

# A = Rock
# B = Paper
# C = Scissors

# 1 for Rock, 2 for Paper, and 3 for Scissors

for line in data:

    if line[2] == "X": # Lose
        score += 0
        if line[0] == "A":
            score += 3
        elif line[0] == "B":
            score += 1
        else:
            score += 2

    elif line[2] == "Y": # Draw
        score += 3
        if line[0] == "A":
            score += 1
        elif line[0] == "B":
            score += 2
        else:
            score += 3

    elif line[2] == "Z": # Win
        score += 6
        if line[0] == "A":
            score += 2
        elif line[0] == "B":
            score += 3
        else:
            score += 1

print(score)