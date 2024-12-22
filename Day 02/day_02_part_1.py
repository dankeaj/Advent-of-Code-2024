# Read in puzzle input
data = open("input.txt", "r")
lines = data.readlines()
data.close()

safe_count = 0
for line in lines:
    safe = True
    
    # Prepare levels
    line = line.strip()
    levels_str = line.split(" ")
    levels = []
    for value in levels_str: levels.append(int(value))
    
    # Determine if the report is differing by amounts 1-3
    for x in range(len(levels)):
        if x >= len(levels) - 1: break
        distance = abs(levels[x+1] - levels[x])
        if distance > 3 or distance < 1:
            safe = False
            break
    
    # Determine if the report is all increasing or all decreasing
    ascending = False
    descending = False
    if sorted(levels) == levels: ascending = True
    if sorted(levels, reverse=True) == levels: descending = True
    if ascending == descending: safe = False # If both ascending and decending are false (or somehow true), then the level is not safe.

    # If the report satisfies the above checks, increment the count
    if safe: safe_count += 1

# Display answer
print("Safe reports: " + str(safe_count))