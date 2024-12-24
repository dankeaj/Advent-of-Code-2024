# Read in puzzle input
data = open("input.txt", "r")
lines = data.readlines()
data.close()

# Difference function, returns the problem level index, or -1 if it's safe
def check_difference(levels):
    for x in range(len(levels)):
        if x >= len(levels) - 1: break
        distance = abs(levels[x+1] - levels[x])
        if distance > 3 or distance < 1:
            return False
    return True

# Ascending function, returns the problem level index, or -1 if it's safe
def check_ascending(levels):
    for x in range(len(levels)):
        if x == 0: continue
        if levels[x] <= levels[x-1]: return False
    return True

# Descending function, returns the problem level index, or -1 if it's safe
def check_descending(levels):
    for x in range(len(levels)):
        if x == 0: continue
        if levels[x] >= levels[x-1]: return False
    return True

# Determines if a passed report is safe.
def check_safe(levels):
    if not check_difference(levels): return False
    if not check_ascending(levels) and not check_descending(levels): return False
    return True

# Returns all possible sub-reports
def generate_subreports(levels):
    result = []
    for x in range(len(levels)):
        temp = levels.copy()
        temp.pop(x)
        result.append(temp)
    return result

# Check reports
safe_count = 0
for line in lines:
    
    # Prepare levels
    line = line.strip()
    levels_str = line.split(" ")
    levels = []
    for value in levels_str: levels.append(int(value))
    
    # See if report is safe
    if check_safe(levels): safe_count += 1
    else:
        # Report is unsafe, see if the problem damper can fix it
        sublevels = generate_subreports(levels)
        for subreport in sublevels:
            if check_safe(subreport):
                safe_count += 1
                break

# # Display answer
print("Safe reports: " + str(safe_count))