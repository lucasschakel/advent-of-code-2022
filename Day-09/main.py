motions_H = []
motions_T = []
last_step_H = [0,0] 
last_step_T = [0,0]

# Add start positions.
motions_H.append(last_step_H) 
motions_T.append(last_step_T) 

# For head: Function to step and save where has been stepped.
def head_stepper(direction, steps, last_step_H):
    if direction == 'R':
        for step in range(0, steps):
            motions_H.append([(last_step_H[0] + step+1), last_step_H[1]])
            tail_follower(motions_H[-1], motions_T[-1])
        return(motions_H[-1])
    elif direction == 'L':
        for step in range(0, steps):
            motions_H.append([(last_step_H[0] - step-1), last_step_H[1]])
            tail_follower(motions_H[-1], motions_T[-1])
        return(motions_H[-1])
    elif direction == 'U':
        for step in range(0, steps):
            motions_H.append([last_step_H[0], (last_step_H[1] + step+1)])
            tail_follower(motions_H[-1], motions_T[-1]) 
        return(motions_H[-1])
    elif direction == 'D':
        for step in range(0, steps):
            motions_H.append([last_step_H[0], (last_step_H[1] - step-1)])
            tail_follower(motions_H[-1], motions_T[-1])
        return(motions_H[-1])

# Function to make the tail follow
def tail_follower(last_step_H, last_step_T):   
    # Head and tail on top of each other.
    if last_step_H == last_step_T:
        return(last_step_T)
    # Head 2 steps directly above tail. Tail has to move 1 step up
    elif last_step_H[0] == last_step_T[0] and last_step_H[1] == last_step_T[1]+2:
        motions_T.append([last_step_T[0], (last_step_T[1]+1)])
        return(motions_T[-1])
    # Head 2 steps under of tail. Tail has to move 1 step down
    elif last_step_H[0] == last_step_T[0] and last_step_H[1]+2 == last_step_T[1]:
        motions_T.append([last_step_T[0], (last_step_T[1]-1)])
        return(motions_T[-1])
    # Head 2 steps left of tail. Tail has to move 1 step left
    elif last_step_H[0]+2 == last_step_T[0] and last_step_H[1] == last_step_T[1]:
        motions_T.append([(last_step_T[0]-1), last_step_T[1]])
        return(motions_T[-1])
    # Head 2 steps right of tail. Tail has to move 1 step right
    elif last_step_H[0] == last_step_T[0]+2 and last_step_H[1] == last_step_T[1]:
        motions_T.append([(last_step_T[0]+1), last_step_T[1]])
        return(motions_T[-1])
    # Head NW diagonal of tail. Move tail one left, one up
    elif last_step_H[0]+1 == last_step_T[0] and last_step_H[1] == last_step_T[1]+2 or last_step_H[0]+2 == last_step_T[0] and last_step_H[1] == last_step_T[1]+1:
        motions_T.append([last_step_T[0]-1, last_step_T[1]+1])
        return(motions_T[-1])
    # Head NE diagonal of tail. Move tail one right, one up
    elif last_step_H[0] == last_step_T[0]+1 and last_step_H[1] == last_step_T[1]+2 or last_step_H[0] == last_step_T[0]+2 and last_step_H[1] == last_step_T[1]+1:
        motions_T.append([last_step_T[0]+1, last_step_T[1]+1])
        return(motions_T[-1])
    # Head SW diagonal of tail. Move tail one left, one down
    elif last_step_H[0]+1 == last_step_T[0] and last_step_H[1]+2 == last_step_T[1] or last_step_H[0]+2 == last_step_T[0] and last_step_H[1]+1 == last_step_T[1]:
        motions_T.append([last_step_T[0]-1, last_step_T[1]-1])
        return(motions_T[-1])
    # Head SE diagonal of tail. Move tail one right, one down
    elif last_step_H[0] == last_step_T[0]+1 and last_step_H[1]+2 == last_step_T[1] or last_step_H[0] == last_step_T[0]+2 and last_step_H[1]+1 == last_step_T[1]:
        motions_T.append([last_step_T[0]+1, last_step_T[1]-1])
        return(motions_T[-1])

with open('input.txt') as f:
    for line in f:
        direction = line.split()[0]
        steps = int(line.split()[1])
        # Solve puzzle 1
        last_step_H = head_stepper(direction, steps, last_step_H)
# Print unique visited steps
subset_list = set(tuple(sublist) for sublist in motions_T)
print(len(subset_list))