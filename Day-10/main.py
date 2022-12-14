with open('input.txt') as f:
    input = f.read().strip().split('\n')

sum_signal_strengths = 0
sprite_location = 1
cycle = 0
CRT = ''

# Solve puzzle 1
def puzzle_1(cycle, sprite_location, sum_signal_strengths):
    for line in input:
        if line == 'noop':
            cycle += 1        
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                sum_signal_strengths += cycle * sprite_location
        else:
            for i in range(2):
                cycle += 1          
                if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                    sum_signal_strengths += cycle * sprite_location     
            sprite_location += int(line.split()[1])
    return(sum_signal_strengths)

# Solve puzzle 2
def puzzle_2(CRT, cycle, sprite_location):
    for line in input:  
        if line == 'noop':
            if cycle%40 == sprite_location or cycle%40 == sprite_location-1 or cycle%40 == sprite_location+1:
                CRT += '▓'
            else:
                CRT += '░'
            cycle += 1
        else:
            for _ in range(2):
                if cycle%40 == sprite_location or cycle%40 == sprite_location-1 or cycle%40 == sprite_location+1:
                    CRT += '▓'
                else:
                    CRT += '░'
                cycle += 1
            sprite_location += int(line.split()[1])
    return(CRT)

# Print solutions
print(puzzle_1(cycle, sprite_location, sum_signal_strengths))
CRT = puzzle_2(CRT, cycle, sprite_location)
for i in range(0, len(CRT), 40):
    print(CRT[i:i+40])

