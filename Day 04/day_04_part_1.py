# Search each row for instances of XMAS forward and backwards
def search_linear(row):
    counted = 0
    for x in range(len(row)):
        if x + 3 > len(row) - 1:
            return counted
        word = row[x] + row[x+1] + row[x+2] + row[x+3]
        if word == "XMAS" or word == "SAMX": counted += 1
    return counted # Should never get called, but for safety reasons I included it

# Read in puzzle input
data = open("input.txt", "r")
lines = data.readlines()
data.close()

# Prepare two dimensional array of word search characters
word_search = []
for line in lines: word_search.append(list(line.strip()))

# Search!
total_found = 0

# Search horizontally
for row in word_search: total_found += search_linear(row)

# Search vertically
for x in range(len(word_search[0])):
    column = []
    for y in range(len(word_search)):
        column.append(word_search[y][x])
    total_found += search_linear(column)

# Search diagonals
# Shoutout to user Flakes on stack overflow for this one
# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
forward_diags = [[] for _ in range(len(word_search) + len(word_search[0]) - 1)]
backward_diags = [[] for _ in range(len(forward_diags))]
min = -(len(word_search)) + 1

for x in range(len(word_search[0])):
    for y in range(len(word_search)):
        forward_diags[x+y].append(word_search[y][x])
        backward_diags[x-y-min].append(word_search[y][x])

for diag in forward_diags:
    if len(diag) > 3: total_found += search_linear(diag)

for diag in backward_diags:
    if len(diag) > 3: total_found += search_linear(diag)

# Display answer
print("Answer: " + str(total_found))
