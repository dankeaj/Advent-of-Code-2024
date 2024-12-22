# Read in puzzle input
data = open("input.txt", "r")
lines = data.readlines()
data.close()

# Setup lists
list_one = []
list_two = []

# prepare lists
for line in lines:
    line = line.strip()
    numbers = line.split("   ")
    list_one.append(int(numbers[0]))
    list_two.append(int(numbers[1]))

list_one.sort()
list_two.sort()

# Calculate total distance
running_total = 0
for position in range(len(list_one)):
    distance = abs(list_one[position] - list_two[position])
    running_total += distance

# Display result
print("Answer: " + str(running_total))