import numpy as np

with open("2022/day-8/input.txt", "r") as f:
    lines = f.readlines()
    lines = [[int(i) for i in l.strip()] for l in lines]

lines = np.array(lines)
rows = lines.shape[0]
cols = lines.shape[1]

number_of_visible_trees = 2 * rows + 2 * cols - 4
for i in range(1, rows-1): #row
    for j in range(1, cols-1): #col
        mid = lines[i, j]
        left = lines[i,j+1:]
        right = lines[i,:j]
        above = lines[:i, j]
        below = lines[i+1:, j]
        visible = np.any([np.all(a < mid) for a in [left, right, above, below]])
        if visible:
            number_of_visible_trees += 1

print(number_of_visible_trees)