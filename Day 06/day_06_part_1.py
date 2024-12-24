# Read in puzzle input
data = open("input.txt", "r")
lines = data.readlines()
data.close()

# Prepare two dimensional array of characters
room = []
for line in lines: room.append(list(line.strip()))

# Holds what direction the guard is facing
#    Up = 0
# Right = 1
#  Down = 2
#  Left = 3
direction = 0

# Figure out where we are starting
current_row = 0
current_col = 0
for row in range(len(room)):
    for character in range(len(room[row])):
        if room[row][character] == "^":
            current_row = row
            current_col = character

# Replace the starting position with an X
room[current_row][current_col] = "X"

exit_flag = True
while exit_flag:
    match direction:
        # Up
        case 0:
            if current_row == 0:
                exit_flag = False
                break
            if room[current_row - 1][current_col] != "#":
                room[current_row - 1][current_col] = "X"
                current_row -= 1
            else:
                direction += 1
        
        # Right
        case 1:
            if current_col == len(room[0]) - 1:
                exit_flag = False
                break
            if room[current_row][current_col + 1] != "#":
                room[current_row][current_col + 1] = "X"
                current_col += 1
            else:
                direction += 1
        
        # Down
        case 2:
            if current_row == len(room) - 1:
                exit_flag = False
                break
            if room[current_row + 1][current_col] != "#":
                room[current_row + 1][current_col] = "X"
                current_row += 1
            else:
                direction += 1
        
        # Left
        case 3:
            if current_col == 0:
                exit_flag = False
                break
            if room[current_row][current_col - 1] != "#":
                room[current_row][current_col - 1] = "X"
                current_col -= 1
            else:
                direction = 0
            
        case _:
            # Something went horribly wrong
            break

# calculate unique visited positions.
unique = 0
for row in room:
    for character in row:
        if character == "X": unique += 1

# Write the simulated guard path to an output file for neat visuals
with open("output.txt", "w") as f:
    for row in room:
        for character in row:
            f.write(character)
        f.write("\n")

# Display answer
print("Answer: " + str(unique))