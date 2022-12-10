import numpy as np

with open("2022/day-8/input.txt", "r") as f:
    lines = f.readlines()
    lines = [[int(i) for i in l.strip()] for l in lines]

lines = np.array(lines)
rows = lines.shape[0]
cols = lines.shape[1]

def get_viewing_distance(trees, height):
    d = 0
    for tree in trees:
        d += 1
        if tree >= height:
            return d
    return d

top_scenic_view = 0

for i in range(1, rows-1): #row
    for j in range(1, cols-1): #col
        mid = lines[i, j]
        left = lines[i,j+1:]
        right = np.flip(lines[i,:j])
        above = np.flip(lines[:i, j])
        below = lines[i+1:, j]
        viewing_distances = [get_viewing_distance(trees, mid) for trees in [left, right, above, below]]
        if np.prod(viewing_distances) > top_scenic_view:
            top_scenic_view = np.prod(viewing_distances)

print(top_scenic_view)