import re

# Read in puzzle input
data = open("input.txt", "r")
text = data.read()
data.close()

# Find all uncorrupted instances of the function using regex
results = re.findall(r"mul\((\d+),(\d+)\)", text)

# Calculate total
running_total = 0
for x, y in results: running_total += (int(x) * int(y))

# Display Answer
print("Answer: " + str(running_total))