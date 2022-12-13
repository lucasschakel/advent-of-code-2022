with open('input.txt') as f:
    datastream = f.read()

# Function to find an unique marker, since sets can't have duplicate values
def unique(s):
    return len(set(s)) == len(s)

# Function to solve the puzzles: Split markers depending on # of unique chars to find, find first marker with X unique characters, find where it is in the datastream, find the last character of it and print it to the terminal.
def puzzle_solver(datastream, number_of_chars):
    markers = [datastream[x:x+number_of_chars] for x in range(0, len(datastream))]
    
    for marker in markers:
        if unique(marker):
            print(datastream.rfind(marker)+number_of_chars)
            break

puzzle_solver(datastream, 4)
puzzle_solver(datastream, 14)