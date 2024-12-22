# Read in puzzle input
data = open("input.txt", "r")
lines = data.readlines()
data.close()

# Setup lists
list_one = []
list_two = []

# Prepare lists
for line in lines:
    line = line.strip()
    numbers = line.split("   ")
    list_one.append(int(numbers[0]))
    list_two.append(int(numbers[1]))

# Calculate similarity score
similarity_score = 0
for value in list_one:
    amount = list_two.count(value)
    similarity_score += value * amount
    
# Display result
print("Answer: " + str(similarity_score))